from fastapi import APIRouter
from ..config.auth import fastapi_users
from src.api_v1.config.auth import auth_backend
from src.api_v1.schemas.auth import UserRead, UserCreate

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/user",
)