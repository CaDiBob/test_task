from collections import defaultdict

from app.exceptions import (
    ProductInsufficientQuantityException,
    OrderNotFoundException,
)
from app.products.dao import ProductDAO
from app.orders.dao import OrderDAO
from app.orders.schemas import OrderItemShema


class OrderAddService:
    """Сервис обработки заказа"""

    def __init__(self, order_items: list[OrderItemShema]) -> None:
        self.order_items = order_items

    async def add_order(self):
        """Создать заказ"""
        ids = [order_item.product_id for order_item in self.order_items]
        order_items = [
            order_item.model_dump() for order_item in self.order_items
        ]
        products = await ProductDAO.find_by_ids(ids)
        await self.check_products(products)
        order_id = await OrderDAO.add(
            status='processing',
            order_items=order_items,
        )
        return order_id

    async def check_products(self, products: list[dict]) -> None:
        """Проверить наличие продукта"""
        for product, order_item in zip(products, self.order_items):
            if product['qty'] < order_item.product_qty:
                raise ProductInsufficientQuantityException(
                    f'{product["name"]} id '
                    f'{product["id"]} недостаточно на складе'
                )


class OrderGetService:
    """Сервис получения заказов"""

    async def get_orders(self, **kwargs) -> list[dict]:
        """Получить заказы
        """
        orders = await OrderDAO.find_all(**kwargs)
        grouped_orders = defaultdict(list)
        for order in orders:
            product_info = {
                'product_id': order['product_id'],
                'name': order['name'],
                'order_qty': order['order_qty'],
                'stock': order['stock'],
                'status': order['status'],
                'created_at': order['created_at'],
            }
            grouped_orders[order['id']].append(product_info)
        return [{'id': order_id,
                 'status': product['status'],
                 'created_at': product['created_at'],
                 'order_items': products}
                for order_id, products in grouped_orders.items()
                for product in products]

    async def get_order(self, order_id: int) -> dict:

        """Получить заказ по id"""
        try:
            order, *_ = await self.get_orders(id=order_id)
        except ValueError:
            raise OrderNotFoundException(
                f'Заказ id {order_id} не найден'
            )
        return order
