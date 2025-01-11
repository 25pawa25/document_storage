from typing import List, Optional

from fastapi import APIRouter, Depends, Query, status

from schemas.response.analytics import AnalyticsResponse
from services.analytics.abc_analytics import AbstractAnalyticsService

router = APIRouter(prefix="/analytic", tags=["Analytic actions"])


@router.get(
    "",
    summary="Get analytic",
    description="Get analytic by queries",
    status_code=status.HTTP_200_OK,
)
async def get_analytics(
    limit: Optional[int] = Query(3, ge=1, le=100),
    analytics_service: AbstractAnalyticsService = Depends(),
) -> List[AnalyticsResponse]:
    """
    Check analytics by queries.
    Args:
        limit: Limit the number of results.
        analytics_service: Analytics service.
    Returns:
        Analytics results.
    """
    return await analytics_service.get_analytics(limit=limit)
