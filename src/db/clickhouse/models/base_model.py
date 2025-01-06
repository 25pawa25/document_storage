from clickhouse_sqlalchemy import get_declarative_base
from sqlalchemy import MetaData
from sqlalchemy.orm import mapped_column

Column = mapped_column

metadata_obj = MetaData()

BaseModel = get_declarative_base(metadata=metadata_obj)
