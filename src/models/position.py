from typing import TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .user import User


class Position(Base):
    __tablename__ = 'position'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    users: Mapped[list["User"]] = relationship(back_populates="positions", secondary="user_position")
