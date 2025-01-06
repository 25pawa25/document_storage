import base64
import gzip
import os

import magic
from fastapi import Request

from common.exceptions.document import InvalidDocument
from schemas.request.document import DocumentRequest


class FileInfo:
    async def __call__(self, request: Request):
        form = await request.form()
        file = form.get("file")

        content = await file.read()
        try:
            content_str = base64.b64encode(gzip.compress(content)).decode("utf-8")
        except UnicodeDecodeError:
            raise InvalidDocument("Unable to decode file content as UTF-8")

        basename = os.path.basename(file.filename)
        size = file.size
        file_format = magic.from_buffer(content, mime=True)
        return DocumentRequest(
            title=os.path.splitext(basename)[0],
            content=content_str,
            type=os.path.splitext(basename)[1].lower(),
            file_format=file_format,
            size=size,
        )
