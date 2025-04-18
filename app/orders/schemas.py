from datetime import datetime

from pydantic import BaseModel


class OrderItemShema(BaseModel):
    product_id: int
    product_qty: int


class OrderItemOutSchema(BaseModel):
    product_id: int
    name: str
    order_qty: int
    stock: int


class OrderOutSchema(BaseModel):
    id: int
    status: str
    created_at: datetime
    order_items: list[OrderItemOutSchema]


class OrderSchema(BaseModel):
    order_id: int
