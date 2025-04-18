from sqlalchemy import select, insert, delete, update

from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.products.models import ProductModel


class ProductDAO(BaseDAO):
    model = ProductModel

    @classmethod
    async def find_product(cls, model_id: int, qty: int) -> dict:
        async with async_session_maker() as session:
            query = (select(cls.model.__table__.columns)
                     .where(id=model_id, qty=qty))
            result = await session.execute(query)
            return result.mappings()
