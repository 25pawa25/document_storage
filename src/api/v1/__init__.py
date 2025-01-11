from fastapi import APIRouter

from api.v1.analytics import analytics_routers
from api.v1.documents import documents_routers

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(analytics_routers)
v1_router.include_router(documents_routers)
