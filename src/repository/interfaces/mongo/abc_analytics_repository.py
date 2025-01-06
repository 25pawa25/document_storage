from abc import ABC, abstractmethod


class AbstractAnalyticsRepository(ABC):
    @abstractmethod
    async def add_query(self, query: str) -> dict:
        pass

    @abstractmethod
    async def get_queries(self, limit: int) -> list:
        pass
