from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from config.database.db_helper import db_helper


async def user_repositories(session: AsyncSession = Depends(db_helper.get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)