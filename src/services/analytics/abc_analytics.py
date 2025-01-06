from abc import ABC, abstractmethod


class AbstractAnalyticsService(ABC):
    @abstractmethod
    async def add_query_to_analytics(self, query: str) -> dict:
        ...

    @abstractmethod
    async def get_analytics(self, limit: int = 3) -> list:
        ...
