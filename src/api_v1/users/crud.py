from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from src.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from config.database.db_helper import db_helper


async def user_crud(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    yield SQLAlchemyUserDatabase(session, User)