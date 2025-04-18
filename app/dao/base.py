from sqlalchemy import select, insert, delete, update

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by) -> dict:
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **values) -> dict:
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(**values)
            new = await session.execute(stmt)
            await session.commit()
            return new.scalar()

    @classmethod
    async def delete(cls, model_id: int) -> None:
        async with async_session_maker() as session:
            stmt = delete(cls.model).where(cls.model.id == model_id)
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def update(cls, model_id: int, **values) -> dict:
        async with async_session_maker() as session:
            stmt = (update(cls.model.__table__)
                    .where(cls.model.id == model_id)
                    .values(**values))
            await session.execute(stmt)
            await session.commit()

    @classmethod
    async def find_by_ids(cls, ids: list) -> dict:
        async with async_session_maker() as session:
            query = (select(cls.model.__table__.columns)
                     .where(cls.model.id.in_(ids)))
            result = await session.execute(query)
            return result.mappings().all()
