from datetime import datetime
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel


class DocumentRequest(BaseModel):
    title: str
    content: str
    type: str
    file_format: str
    size: int
    created_at: Optional[datetime] = Field(datetime.utcnow())
