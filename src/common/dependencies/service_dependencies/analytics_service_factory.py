from clickhouse_connect.driver import AsyncClient
from fastapi import Depends

from common.dependencies.registrator import add_factory_to_mapper
from db.clickhouse.connection import get_async_clickhouse_client
from repository.clickhouse_implementation.analytics_repository import (
    AnalyticsRepository,
)
from services.analytics.abc_analytics import AbstractAnalyticsService
from services.analytics.analytics import AnalyticsService


@add_factory_to_mapper(AbstractAnalyticsService)
def create_analytics_service(
    client: AsyncClient = Depends(get_async_clickhouse_client),
):
    return AnalyticsService(
        analytics_repository=AnalyticsRepository(client=client),
    )
