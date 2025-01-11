from functools import lru_cache

from pydantic import BaseSettings, Field


# Project name. Used in Swagger documentation
class ProjectConfig(BaseSettings):
    name: str = Field("document_storage", env="PROJECT_NAME")
    api_host: str = Field(default="127.0.0.1", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")
    debug: bool = Field(default=False, env="DEBUG")
    enable_tracer: bool = Field(False, env="ENABLE_TRACER")


# ClickHouse
class ClickHouseConfig(BaseSettings):
    host: str = Field("clickhouse", env="CLICKHOUSE_HOST")
    port: str = Field(default="8123", env="CLICKHOUSE_PORT")
    db_name: str = Field(default="documents_db", env="CLICKHOUSE_DATABASE")
    user: str = Field(default="user", env="CLICKHOUSE_USER")
    password: str = Field(default="changeme", env="CLICKHOUSE_PASSWORD")

    @property
    def migration_database_url(self):
        return f"clickhouse://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


# MongoDB
class MongoDBConfig(BaseSettings):
    host: str = Field("mongodb", env="MONGODB_HOST")
    port: str = Field(default="27017", env="MONGODB_PORT")
    db_name: str = Field(default="analytics_db", env="MONGODB_DATABASE")
    user: str = Field(default="user", env="MONGODB_USER")
    password: str = Field(default="changeme", env="MONGODB_PASSWORD")

    @property
    def connection_url(self):
        return f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


class Settings(BaseSettings):
    project: ProjectConfig = ProjectConfig()
    clickhouse: ClickHouseConfig = ClickHouseConfig()
    mongodb: MongoDBConfig = MongoDBConfig()


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
