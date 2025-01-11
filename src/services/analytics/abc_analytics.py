from abc import ABC, abstractmethod
from typing import List

from schemas.request.analytics import AnalyticsRequest
from schemas.response.analytics import AnalyticsResponse


class AbstractAnalyticsService(ABC):
    @abstractmethod
    async def add_query_to_analytics(self, analytics: AnalyticsRequest):
        ...

    @abstractmethod
    async def get_analytics(self, limit: int = 3) -> List[AnalyticsResponse]:
        ...
