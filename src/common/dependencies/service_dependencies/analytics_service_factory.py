from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from common.dependencies.registrator import add_factory_to_mapper
from db.mongodb.connection import get_async_mongodb_client
from repository.mongo_implementation.analytics_repository import AnalyticsRepository
from services.analytics.abc_analytics import AbstractAnalyticsService
from services.analytics.analytics import AnalyticsService


@add_factory_to_mapper(AbstractAnalyticsService)
def create_analytics_service(
    client: AsyncIOMotorClient = Depends(get_async_mongodb_client),
):
    return AnalyticsService(
        analytics_repository=AnalyticsRepository(client=client),
    )
