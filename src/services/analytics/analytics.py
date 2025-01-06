from repository.interfaces.mongo.abc_analytics_repository import (
    AbstractAnalyticsRepository,
)
from services.analytics.abc_analytics import AbstractAnalyticsService


class AnalyticsService(AbstractAnalyticsService):
    def __init__(self, analytics_repository: AbstractAnalyticsRepository):
        self.analytics_repository = analytics_repository

    async def add_query_to_analytics(self, query: str) -> dict:
        return await self.analytics_repository.add_query(query)

    async def get_analytics(self, limit: int = 3) -> list:
        return await self.analytics_repository.get_queries(limit)
