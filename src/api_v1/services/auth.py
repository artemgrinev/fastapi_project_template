from fastapi import Depends
from fastapi_users import BaseUserManager, IntegerIDMixin

from src.api_v1.repositories.auth import user_repositories
from src.models.user import User
from config.project_config import settings


SECRET = settings.JWT


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET


async def user_manager(user_db=Depends(user_repositories)):
    yield UserManager(user_db)

