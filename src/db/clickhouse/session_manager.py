import contextlib

from asynch.connection import Connection
from clickhouse_connect import get_async_client

from db.base.abc_async_session_manager import BaseAsyncSessionManager


class ClickHouseSessionManager(BaseAsyncSessionManager):
    def __init__(self) -> None:
        self._sessionmaker = None

    def init(
        self, host: str, port: int, db_name: str, user: str, password: str
    ) -> None:
        """
        Init sessionmaker of clickhouse database
        Args:
            host: clickhouse host
            port: clickhouse port
            db_name: clickhouse database
            user: clickhouse user
            password: clickhouse password
        """
        self._sessionmaker = self._clickhouse_sessionmaker(
            host, port, db_name, user, password
        )

    @staticmethod
    def _clickhouse_sessionmaker(
        host: str, port: int, db_name: str, user: str, password: str
    ):
        """
        Init clickhouse session
        Args:
            host: clickhouse host
            port: clickhouse port
            db_name: clickhouse database
            user: clickhouse user
            password: clickhouse password
        Returns:
            clickhouse sessionmaker(function)
        """

        async def client():
            return await get_async_client(
                host=host, port=port, database=db_name, username=user, password=password
            )

        return client

    def close(self) -> None:
        """
        Delete sessionmaker of clickhouse database
        Returns:
            None
        """
        self._sessionmaker = None

    @contextlib.asynccontextmanager
    async def async_session(self) -> Connection:
        """
        Get session of clickhouse database
        Returns:
            yield session of clickhouse database
        """
        if self._sessionmaker is None:
            raise IOError("DatabaseSessionManager is not initialized")

        connection = await self._sessionmaker()
        try:
            yield connection
        finally:
            connection.close()


clickhouse_db_manager = ClickHouseSessionManager()
