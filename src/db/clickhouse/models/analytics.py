import uuid

from clickhouse_sqlalchemy import engines, types

from db.clickhouse.models.base_model import BaseModel, Column


class Analytics(BaseModel):
    __tablename__ = "analytics"
    __table_args__ = (
        engines.MergeTree(
            primary_key=["id"],
            order_by=["created_at"],
        ),
    )
    id = Column(types.UUID, primary_key=True, default=uuid.uuid4)
    query = Column(types.String, nullable=False)
    method = Column(types.String, nullable=False)
    ip = Column(types.String, nullable=False)
    user_agent = Column(types.String, nullable=False)
    created_at = Column(types.DateTime, nullable=False)
