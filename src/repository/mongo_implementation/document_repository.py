import base64
import gzip
from typing import List, Optional

from repository.interfaces.mongo.abc_document_repository import (
    AbstractDocumentRepository,
)
from repository.mongo_implementation.base_repository import BaseRepository


class DocumentRepository(AbstractDocumentRepository, BaseRepository):
    collection_name = "documents"

    async def add_or_update_document(self, **fields) -> dict:
        """
        Add or update a document
        fields:
            fields to add to the document
        Returns:
            dict with the updated document
        """
        result = await self.collection.update_one(
            {"title": fields.get("title")},
            {"$set": fields, "$currentDate": {"last_accessed": True}},
            upsert=True,
        )
        return {
            "matched_count": result.matched_count,
            "modified_count": result.modified_count,
            "upserted_id": result.upserted_id,
        }

    async def get_documents(
        self, limit: int, title: Optional[str] = None
    ) -> List[dict]:
        """
        Retrieves documents based on title or returns the most recent documents.
            limit: Number of documents to return.
            title: Optional title to filter documents by.
        returns:
            list of documents info
        """
        filter_criteria = {"title": title} if title else {}
        cursor = (
            self.collection.find(filter_criteria, {"_id": 0})
            .sort("created_at", -1)
            .limit(limit)
        )
        documents = await cursor.to_list(length=limit)

        for document in documents:
            if content := document.get("content"):
                try:
                    document["content"] = gzip.decompress(
                        base64.b64decode(content.encode("utf-8"))
                    ).decode("utf-8")
                except UnicodeDecodeError:
                    document["content"] = content
        return documents

    async def delete_document(self, title: str) -> dict:
        """
        Deletes a document by title.
        args:
            title: The title of the document to be deleted.
        returns:
            Count of deleted documents.
        """
        result = await self.collection.delete_one({"title": title})
        return result.deleted_count
