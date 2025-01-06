from abc import ABC, abstractmethod

from schemas.entities.document import DocumentEntity


class AbstractDocumentRepository(ABC):
    @abstractmethod
    async def add_document(self, **fields):
        pass

    @abstractmethod
    async def get_document(
        self, raise_if_notfound: bool = True, **fields
    ) -> DocumentEntity:
        pass

    @abstractmethod
    async def delete_document(self, title: str):
        pass
