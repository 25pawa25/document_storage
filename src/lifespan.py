import contextlib
from typing import AsyncIterator

from fastapi import FastAPI

from core.config import settings
from db.clickhouse.session_manager import clickhouse_db_manager
from db.mongodb.session_manager import mongodb_manager


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    clickhouse_db_manager.init(
        settings.clickhouse.host,
        settings.clickhouse.port,
        settings.clickhouse.db_name,
        settings.clickhouse.user,
        settings.clickhouse.password,
    )
    await mongodb_manager.init(settings.mongodb.connection_url)
    yield
    clickhouse_db_manager.close()
    await mongodb_manager.close()
