from repository.interfaces.clickhouse.abc_document_repository import (
    AbstractDocumentRepository,
)
from schemas.request.document import DocumentRequest
from schemas.response.document import DocumentResponse
from services.document.abc_document import AbstractDocumentService


class DocumentService(AbstractDocumentService):
    def __init__(self, document_repository: AbstractDocumentRepository):
        self.document_repository = document_repository

    async def create_document(self, document: DocumentRequest):
        await self.document_repository.add_document(**document.dict())

    async def get_document(self, title: str, file_type: str = None) -> DocumentResponse:
        document_db = await self.document_repository.get_document(
            title=title, type=file_type
        )
        return DocumentResponse.from_entity(document_db)

    async def delete_document(self, title: str):
        await self.document_repository.delete_document(title)
