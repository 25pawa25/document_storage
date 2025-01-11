from abc import ABC, abstractmethod
from typing import List, Optional


class AbstractDocumentRepository(ABC):
    @abstractmethod
    async def add_or_update_document(self, **fields) -> dict:
        pass

    @abstractmethod
    async def get_documents(
        self, limit: int, title: Optional[str] = None
    ) -> List[dict]:
        pass

    @abstractmethod
    async def delete_document(self, title: str) -> int:
        pass
