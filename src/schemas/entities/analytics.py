import uuid
from datetime import datetime

from schemas.entities.base_entity import BaseEntity


class AnalyticsEntity(BaseEntity):
    id: uuid.UUID
    query: str
    method: str
    ip: str
    user_agent: str
    created_at: datetime

    class Config:
        orm_mode = True
