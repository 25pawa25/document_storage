from abc import ABC, abstractmethod
from typing import Optional

from schemas.request.document import DocumentRequest


class AbstractDocumentService(ABC):
    @abstractmethod
    async def add_or_update_document(self, document: DocumentRequest) -> dict:
        ...

    @abstractmethod
    async def get_documents(
        self, title: Optional[str] = None, limit: int = None
    ) -> list:
        ...

    @abstractmethod
    async def delete_document(self, title: str) -> int:
        ...
