from datetime import datetime
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel


class AnalyticsRequest(BaseModel):
    query: str
    method: str
    ip: str
    user_agent: str
    created_at: Optional[datetime] = Field(datetime.utcnow())
