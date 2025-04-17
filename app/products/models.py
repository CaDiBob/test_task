from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class ProductModel(Base):

    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    qty: Mapped[int]
