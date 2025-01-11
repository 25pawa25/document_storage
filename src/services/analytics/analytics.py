from typing import List

from repository.interfaces.clickhouse.abc_analytics_repository import (
    AbstractAnalyticsRepository,
)
from schemas.request.analytics import AnalyticsRequest
from schemas.response.analytics import AnalyticsResponse
from services.analytics.abc_analytics import AbstractAnalyticsService


class AnalyticsService(AbstractAnalyticsService):
    def __init__(self, analytics_repository: AbstractAnalyticsRepository):
        self.analytics_repository = analytics_repository

    async def add_query_to_analytics(self, analytics: AnalyticsRequest):
        """
        Adds a query to the analytics
        analytics: AnalyticsRequest
        """
        await self.analytics_repository.add_query(**analytics.dict())

    async def get_analytics(self, limit: int = 3) -> List[AnalyticsResponse]:
        """
        Get all analytics with limit
        return: list of AnalyticsResponse
        """
        analytics_db_list = await self.analytics_repository.get_queries(limit=limit)
        return [
            AnalyticsResponse.from_entity(analytics_db)
            for analytics_db in analytics_db_list
        ]
