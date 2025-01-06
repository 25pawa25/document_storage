import base64
import gzip
from datetime import datetime

from pydantic.main import BaseModel

from schemas.entities.document import DocumentEntity


class DocumentResponse(BaseModel):
    title: str
    content: str
    type: str
    file_format: str
    size: int
    created_at: datetime

    class Config:
        orm_mode = True

    @classmethod
    def from_entity(cls, instance: DocumentEntity) -> "DocumentResponse":
        content_str = gzip.decompress(
            base64.b64decode(instance.content.encode("utf-8"))
        ).decode("utf-8")
        return cls(
            title=instance.title,
            content=content_str,
            type=instance.type,
            file_format=instance.file_format,
            size=instance.size,
            created_at=instance.created_at,
        )
