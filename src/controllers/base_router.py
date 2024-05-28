from fastapi import APIRouter
from src.api_v1.controllers import router as api_v1_routes


def get_apps_router():
    router = APIRouter(
        prefix="/api"
    )
    router.include_router(
        api_v1_routes,
    )
    return router