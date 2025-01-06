from datetime import datetime

from repository.interfaces.mongo.abc_analytics_repository import (
    AbstractAnalyticsRepository,
)
from repository.mongo_implementation.base_repository import BaseRepository


class AnalyticsRepository(AbstractAnalyticsRepository, BaseRepository):
    collection_name = "analytics"

    async def add_query(self, query: str) -> dict:
        """ """
        timestamp = datetime.utcnow()
        result = await self.collection.update_one(
            {"query": query},
            {
                "$set": {"last_accessed": timestamp},
                "$inc": {"count": 1},
            },
            upsert=True,
        )
        return {
            "matched_count": result.matched_count,
            "modified_count": result.modified_count,
            "upserted_id": result.upserted_id,
        }

    async def get_queries(self, limit: int) -> list:
        """ """
        cursor = (
            self.collection.find({}, {"_id": 0, "query": 1, "count": 1})
            .sort("count", -1)
            .limit(limit)
        )
        return await cursor.to_list(length=limit)
