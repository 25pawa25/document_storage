import contextlib

from motor.motor_asyncio import AsyncIOMotorClient

from db.base.abc_async_session_manager import BaseAsyncSessionManager


class MongoDBSessionManager(BaseAsyncSessionManager):
    def __init__(self) -> None:
        self._sessionmaker = None

    async def init(self, url: str) -> None:
        """
        Init sessionmaker of mongodb database
        Args:
            url: mongodb url
        """
        self._sessionmaker = await self._mongodb_sessionmaker(url)

    @staticmethod
    async def _mongodb_sessionmaker(url: str):
        """
        Init mongodb session
        Args:
            url: mongodb url
        Returns:
            mongodb sessionmaker(function)
        """

        async def get_client():
            motor_client: AsyncIOMotorClient = AsyncIOMotorClient(url)
            return motor_client

        return get_client

    async def close(self) -> None:
        """
        Delete sessionmaker of mongodb database
        Returns:
            None
        """
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def async_session(self) -> AsyncIOMotorClient:
        """
        Get session of mongodb database
        Returns:
            yield session of mongodb database
        """
        if self._sessionmaker is None:
            raise IOError("DatabaseSessionManager is not initialized")
        yield self._sessionmaker

    def sync_session(self):
        if self._sessionmaker is None:
            raise IOError("DatabaseSessionManager is not initialized")
        return self._sessionmaker()


mongodb_manager = MongoDBSessionManager()
