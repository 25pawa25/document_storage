from datetime import datetime

from schemas.entities.base_entity import BaseEntity


class DocumentEntity(BaseEntity):
    title: str
    content: str
    type: str
    file_format: str
    size: int
    created_at: datetime

    class Config:
        orm_mode = True
