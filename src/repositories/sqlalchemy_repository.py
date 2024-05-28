from typing import Type, TypeVar, Optional, Generic

from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.base import Base
from config.database.db_helper import db_helper
from .base_repository import AbstractRepository


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    # session: AsyncSession = db_helper.session_dependency()

    def __init__(
            self,
            session: AsyncSession,
            model: Type[ModelType]
        ):
        self.session = session
        self.model = model

    async def add_one(self, data: CreateSchemaType) -> int:
        async with self.session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
        
    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self.session() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
        stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
        res = await self.session.execute(stmt)
        await self.session.commit()
        return res.scalar_one()

    async def delete(self, **filters) -> None:
        await self.session.execute(delete(self.model).filter_by(**filters))
        await self.session.commit()

    async def get_single(self, **filters) -> Optional[ModelType] | None:
        row = await self.session.execute(select(self.model).filter_by(**filters))
        return row.scalar_one_or_none()

    async def get_multi(
            self,
            order: str = "id",
            limit: int = 100,
            offset: int = 0
    ) -> list[ModelType]:
        stmt = select(self.model).order_by(*order).limit(limit).offset(offset)
        row = await self.session.execute(stmt)
        return row.scalars().all()