from datetime import datetime

from pydantic.main import BaseModel

from schemas.entities.analytics import AnalyticsEntity


class AnalyticsResponse(BaseModel):
    query: str
    method: str
    ip: str
    user_agent: str
    created_at: datetime

    class Config:
        orm_mode = True

    @classmethod
    def from_entity(cls, instance: AnalyticsEntity) -> "AnalyticsResponse":
        return cls(
            query=instance.query,
            method=instance.method,
            ip=instance.ip,
            user_agent=instance.user_agent,
            created_at=instance.created_at,
        )
