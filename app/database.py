from datetime import datetime
from typing_extensions import Annotated

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, sessionmaker, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.config import settings


engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


timestamp = Annotated[
    datetime,
    mapped_column(
        nullable=False,
        server_default=func.CURRENT_TIMESTAMP(),
    ),
]
