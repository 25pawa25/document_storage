from abc import ABC, abstractmethod

from schemas.request.document import DocumentRequest
from schemas.response.document import DocumentResponse


class AbstractDocumentService(ABC):
    @abstractmethod
    async def create_document(self, document: DocumentRequest):
        ...

    @abstractmethod
    async def get_document(self, title: str, file_type: str = None) -> DocumentResponse:
        ...

    @abstractmethod
    async def delete_document(self, title: str):
        ...
