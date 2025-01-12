from fastapi import Depends, Request

from schemas.request.analytics import AnalyticsRequest
from services.analytics.abc_analytics import AbstractAnalyticsService


class AnalyticQuery:
    async def __call__(
        self, request: Request, analytics_service: AbstractAnalyticsService = Depends()
    ):
        method = request.method
        url = str(request.url)
        ip = str(request.client.host)
        user_agent = request.headers.get("User-Agent")
        await analytics_service.add_query_to_analytics(
            AnalyticsRequest(query=url, method=method, ip=ip, user_agent=user_agent)
        )
