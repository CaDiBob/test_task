from sqlalchemy import insert, select, update

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.orders.models import Order, OrderItem
from app.products.models import ProductModel


class OrderDAO(BaseDAO):
    model = Order

    @classmethod
    async def add(cls, status: str, order_items: list[dict]) -> int:
        async with async_session_maker() as session:
            stmt = insert(cls.model).values(status=status).returning(cls.model)
            new_order = await session.execute(stmt)
            await session.commit()
            order = new_order.scalar()
            for order_item in order_items:
                order_item['order_id'] = order.id
            stmt = insert(OrderItem)
            await session.execute(stmt, order_items)
            for product in order_items:
                query = select(ProductModel.qty).filter_by(
                    id=product['product_id']
                )
                qty = await session.execute(query)
                qty: int = qty.scalar()
                new_qty = qty - int(product['product_qty'])
                stmt = (update(ProductModel)
                        .where(ProductModel.id == product['product_id'])
                        .values(qty=new_qty))
                await session.execute(stmt)
            await session.commit()
            return order.id

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        async with async_session_maker() as session:
            query = (
                select(
                    Order.id,
                    Order.status,
                    Order.created_at,
                    OrderItem.product_id,
                    ProductModel.name,
                    OrderItem.product_qty.label('order_qty'),
                    ProductModel.qty.label('stock')
                ).filter_by(**filter_by)
                .join(OrderItem, OrderItem.order_id == Order.id)
                .join(ProductModel, ProductModel.id == OrderItem.product_id)
                .order_by(Order.id)
            )
            result = await session.execute(query)
            return result.mappings().all()
