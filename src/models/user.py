from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .position import Position
    from .profile import Profile


class User(SQLAlchemyBaseUserTable[int], Base):
    user_name: Mapped[str] = mapped_column(String, nullable=False)
    posts: Mapped[list["Position"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")