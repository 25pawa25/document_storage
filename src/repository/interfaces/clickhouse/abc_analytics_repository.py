from abc import ABC, abstractmethod
from typing import List

from schemas.entities.analytics import AnalyticsEntity


class AbstractAnalyticsRepository(ABC):
    @abstractmethod
    async def add_query(self, **fields):
        pass

    @abstractmethod
    async def get_queries(
        self, limit: int = 10, desc: bool = True, **filters
    ) -> List[AnalyticsEntity]:
        pass
