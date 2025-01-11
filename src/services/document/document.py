from typing import Optional

from repository.interfaces.mongo.abc_document_repository import (
    AbstractDocumentRepository,
)
from schemas.request.document import DocumentRequest
from services.document.abc_document import AbstractDocumentService


class DocumentService(AbstractDocumentService):
    def __init__(self, document_repository: AbstractDocumentRepository):
        self.document_repository = document_repository

    async def add_or_update_document(self, document: DocumentRequest) -> dict:
        """
        Add or update a document or update a document.
        document: DocumentRequest
        Returns:
            dict
        """
        return await self.document_repository.add_or_update_document(**document.dict())

    async def get_documents(self, title: Optional[str] = None, limit: int = 3) -> list:
        """
        Get document by title or documents with limit.
        title: title to filter documents by
        limit: number of documents to return
        Returns:
            list of documents
        """
        return await self.document_repository.get_documents(limit, title)

    async def delete_document(self, title: str) -> int:
        """
        Delete a document by title.
        title: title to filter documents by
        Returns:
            count of deleted documents
        """
        return await self.document_repository.delete_document(title)
