from fastapi import Depends, Request

from services.analytics.abc_analytics import AbstractAnalyticsService


class AnalyticQuery:
    async def __call__(
        self, request: Request, analytics_service: AbstractAnalyticsService = Depends()
    ):
        method = request.method
        url = str(request.url)
        await analytics_service.add_query_to_analytics(f"{method}:{url}")
