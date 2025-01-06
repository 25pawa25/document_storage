from clickhouse_connect.driver import AsyncClient
from fastapi import Depends

from common.dependencies.registrator import add_factory_to_mapper
from db.clickhouse.connection import get_async_clickhouse_client
from repository.clickhouse_implementation.document_repository import DocumentRepository
from services.document.abc_document import AbstractDocumentService
from services.document.document import DocumentService


@add_factory_to_mapper(AbstractDocumentService)
def create_document_service(client: AsyncClient = Depends(get_async_clickhouse_client)):
    return DocumentService(
        document_repository=DocumentRepository(client=client),
    )
