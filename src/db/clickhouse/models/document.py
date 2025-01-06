from clickhouse_sqlalchemy import engines, types
from sqlalchemy import PrimaryKeyConstraint

from db.clickhouse.models.base_model import BaseModel, Column


class Document(BaseModel):
    __tablename__ = "document"
    __table_args__ = (
        engines.ReplacingMergeTree(
            primary_key=["title", "file_format", "type", "size"],
            order_by=["title", "file_format", "type", "size", "created_at"],
        ),
        PrimaryKeyConstraint("title", "file_format", "type", "size"),
    )
    title = Column(types.String, nullable=False)
    content = Column(types.String, nullable=False)
    type = Column(types.String, nullable=False)
    file_format = Column(types.String, nullable=False)
    size = Column(types.Int32, nullable=False)
    created_at = Column(types.DateTime, nullable=False)
