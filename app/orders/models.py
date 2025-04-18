from typing_extensions import Literal


from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, timestamp


Status = Literal['processing', 'sending', 'delivered']


class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[timestamp]
    status: Mapped[Status]
    order_items: Mapped[list['OrderItem']] = relationship(
        back_populates='order'
    )


class OrderItem(Base):

    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    product_qty: Mapped[int]
    order: Mapped['Order'] = relationship(back_populates='order_items')
