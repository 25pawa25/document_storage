import backoff
from motor.motor_asyncio import AsyncIOMotorClient

from db.mongodb.session_manager import mongodb_manager


@backoff.on_exception(backoff.expo, RuntimeError, max_time=30)
async def get_async_mongodb_client() -> AsyncIOMotorClient:
    async with mongodb_manager.async_session() as session:
        return await session()
