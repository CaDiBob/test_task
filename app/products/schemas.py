from typing_extensions import Optional

from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    qty: int


class ErrorMessageSchema(BaseModel):
    message: str
