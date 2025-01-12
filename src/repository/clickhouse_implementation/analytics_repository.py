from typing import List

from db.clickhouse.models import Analytics
from repository.clickhouse_implementation.base_repository import BaseRepository
from repository.interfaces.clickhouse.abc_analytics_repository import (
    AbstractAnalyticsRepository,
)
from schemas.entities.analytics import AnalyticsEntity


class AnalyticsRepository(AbstractAnalyticsRepository, BaseRepository):
    class_model = Analytics
    entity_class = AnalyticsEntity
    table_name = "analytics"

    async def add_query(self, **fields):
        """
        Add a request query to the analytics.
        kwargs:
            fields: Analytics fields to add.
        """
        columns = ", ".join(fields.keys())
        placeholders = ", ".join([f"%({key})s" for key in fields.keys()])

        query = f"""
               INSERT INTO {self.table_name} ({columns})
               VALUES ({placeholders})
               """

        await self._client.command(query, fields)

    async def get_queries(
        self, limit: int = 10, desc: bool = True, **filters
    ) -> List[AnalyticsEntity]:
        """
        Get analytics of requests.
        kwargs:
            limit: Number of records to return.
            order_by: Field to order by.
            desc: Order direction, descending if True.
            filters: Conditions to filter the queries.
        Returns:
            List[AnalyticsEntity]: List of analytics records.
        """
        filter_conditions = " AND ".join([f"{key} = %({key})s" for key in filters])
        order_direction = "DESC" if desc else "ASC"
        where_clause = f"WHERE {filter_conditions}" if filter_conditions else ""

        query = f"""
        SELECT * FROM {self.table_name}
        {where_clause}
        ORDER BY created_at {order_direction}
        LIMIT {limit}
        """

        result = await self._client.query(query, parameters=filters)
        if rows := result.result_rows:
            return [self.to_entity(row) for row in rows]
