from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from common.dependencies.registrator import add_factory_to_mapper
from db.mongodb.connection import get_async_mongodb_client
from repository.mongo_implementation.document_repository import DocumentRepository
from services.document.abc_document import AbstractDocumentService
from services.document.document import DocumentService


@add_factory_to_mapper(AbstractDocumentService)
def create_document_service(
    client: AsyncIOMotorClient = Depends(get_async_mongodb_client),
):
    return DocumentService(
        document_repository=DocumentRepository(client=client),
    )
