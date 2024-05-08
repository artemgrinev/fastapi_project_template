from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from .mixins import UserRelationMixin


class UserPosition(Base, UserRelationMixin):
    __tablename__ = "user_position"
    _primary_key = True
    position_id: Mapped[int] = mapped_column(ForeignKey("position.id"), primary_key=True, nullable=False)

