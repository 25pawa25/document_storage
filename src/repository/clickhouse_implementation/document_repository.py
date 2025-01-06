from common.exceptions.document import DocumentDoesNotExist
from db.clickhouse.models import Document
from repository.clickhouse_implementation.base_repository import BaseRepository
from repository.interfaces.clickhouse.abc_document_repository import (
    AbstractDocumentRepository,
)
from schemas.entities.document import DocumentEntity


class DocumentRepository(AbstractDocumentRepository, BaseRepository):
    class_model = Document
    entity_class = DocumentEntity
    table_name = "document"

    async def add_document(self, **fields):
        """
        Add a document to the ClickHouse table.
        kwargs:
            fields: Document fields to add.
        """
        columns = ", ".join(fields.keys())
        placeholders = ", ".join([f"%({key})s" for key in fields.keys()])

        query = f"""
               INSERT INTO {self.table_name} ({columns})
               VALUES ({placeholders})
               """

        await self._client.command(query, fields)

    async def get_document(
        self, raise_if_notfound: bool = True, **fields
    ) -> DocumentEntity:
        """
        Retrieve a document by its title.
        args:
            title: Title of the document.
        Returns:
            DocumentEntity
        """
        conditions = " AND ".join(
            [
                f"{field_item[0]} = %({field_item[0]})s"
                for field_item in fields.items()
                if field_item[1]
            ]
        )
        query = f"SELECT * FROM {self.table_name} WHERE {conditions} LIMIT 1"
        result = await self._client.query(query, fields)
        if result.result_rows:
            return self.to_entity(result.result_rows[0])
        if raise_if_notfound:
            raise DocumentDoesNotExist("Document not found", **fields)

    async def delete_document(self, title: str):
        """
        Delete a document by its title.
        args:
            document_id: Title of the document.
        """
        query = f"ALTER TABLE {self.table_name} DELETE WHERE title = %(title)s"
        await self._client.command(query, {"title": title})
