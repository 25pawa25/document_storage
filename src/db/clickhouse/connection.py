import backoff
from clickhouse_connect.driver import AsyncClient

from db.clickhouse.session_manager import clickhouse_db_manager


@backoff.on_exception(backoff.expo, RuntimeError, max_time=30)
async def get_async_clickhouse_client() -> AsyncClient:
    async with clickhouse_db_manager.async_session() as session:
        return session
