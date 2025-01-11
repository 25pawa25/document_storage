from motor.motor_asyncio import AsyncIOMotorClient


class BaseRepository:
    collection_name: str = None

    def __init__(self, client: AsyncIOMotorClient):
        self._client = client
        self.collection = self._client.get_database()[self.collection_name]
