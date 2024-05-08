from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from src.models.user import User
from src.api_v1.users.schemas import UserRead, UserCreate
from src.api_v1.users.dependencies import user_manager
from src.api_v1.users.config import auth_backend




fastapi_users = FastAPIUsers[User, int](
    user_manager,
    [auth_backend],
)


router = APIRouter(
    prefix="/v1",
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)