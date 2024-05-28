from fastapi_users import FastAPIUsers
from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy

from src.api_v1.services.auth import user_manager
from src.models.user import User
from config.project_config import settings


SECRET = settings.JWT


cookie_transport = CookieTransport(
    cookie_max_age=settings.COOCKIE_AGE, 
    cookie_name="fastapi_project_auth_coockie"
)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()