"""Базовый репозиторий — CRUD-операции через SQLAlchemy."""
from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from src.exceptions import ObjectAlreadyExistsException, ObjectNotFoundException


class BaseRepository:
    model = None
    mapper = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_filtered(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return [self.mapper.map_to_domain_entity(row) for row in result.scalars().all()]

    async def get_all(self):
        return await self.get_filtered()

    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        row = result.scalars().one_or_none()
        if row is None:
            return None
        return self.mapper.map_to_domain_entity(row)

    async def get_one(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        try:
            row = result.scalars().one()
        except NoResultFound:
            raise ObjectNotFoundException(f"{self.model.__name__} not found: {filter_by}")
        return self.mapper.map_to_domain_entity(row)

    async def add(self, data: BaseModel):
        try:
            stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
            result = await self.session.execute(stmt)
            return self.mapper.map_to_domain_entity(result.scalars().one())
        except IntegrityError:
            raise ObjectAlreadyExistsException(f"{self.model.__name__} already exists")

    async def add_bulk(self, data: list[BaseModel]):
        stmt = insert(self.model).values([item.model_dump() for item in data])
        await self.session.execute(stmt)

    async def edit(self, data: BaseModel, exclude_unset: bool = False, **filter_by):
        values = data.model_dump(exclude_unset=exclude_unset)
        stmt = update(self.model).filter_by(**filter_by).values(**values).returning(self.model)
        result = await self.session.execute(stmt)
        try:
            return self.mapper.map_to_domain_entity(result.scalars().one())
        except NoResultFound:
            raise ObjectNotFoundException(f"{self.model.__name__} not found: {filter_by}")

    async def delete(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)
