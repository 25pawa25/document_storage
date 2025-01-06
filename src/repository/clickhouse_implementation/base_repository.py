from typing import Any

from clickhouse_connect.driver import AsyncClient

from db.clickhouse.models.base_model import BaseModel
from schemas.entities.base_entity import BaseEntity


class BaseRepository:
    class_model: BaseModel = None
    entity_class: BaseEntity = None
    table_name: str = None

    def __init__(self, client: AsyncClient):
        self._client = client

    def to_entity(self, obj: Any) -> BaseEntity:
        return (
            self.entity_class.parse_obj(
                dict(zip(self.entity_class.__fields__.keys(), obj))
            )
            if obj
            else None
        )
