import asyncio
from typing import AsyncGenerator
from httpx import ASGITransport, AsyncClient
import pytest
import pytest_asyncio
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config

from main import app
from src.models import Base
from config.database.db_helper import db_helper
from config.project_config import settings

DATABASE_TEST_URL = (
    f'postgresql+asyncpg://'
    f'{settings.TEST_POSTGRES_USER}:'
    f'{settings.TEST_POSTGRES_PASSWORD}@'
    f'{settings.TEST_POSTGRES_HOST}:'
    f'{settings.TEST_POSTGRES_PORT}/'
    f'{settings.TEST_POSTGRES_DB}'
)


engine_test = create_async_engine(DATABASE_TEST_URL, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[db_helper.get_async_session] = override_get_async_session

@pytest.fixture(scope="session")
def alembic_config():
    config = Config("alembic.ini")
    config.set_main_option("sqlalchemy.url", DATABASE_TEST_URL)
    return config

@pytest_asyncio.fixture(autouse=True, scope="session")
async def prepare_database(alembic_config):
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        yield
        await conn.run_sync(Base.metadata.create_all)
    
    command.upgrade(alembic_config, "head")

@pytest_asyncio.fixture(scope="session")
async def db_session(prepare_database):
    await prepare_database()
    async with async_session_maker() as session:
        yield session


@pytest_asyncio.fixture(scope="session")
async def async_client() -> AsyncSession:
    async with AsyncClient(base_url="http://test", transport=ASGITransport(app)) as client:
        yield client