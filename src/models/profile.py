import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, Date, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Profile(Base, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "profile"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str | None] = mapped_column(String(40))
    first_name: Mapped[str | None] = mapped_column(String(40))
    birthdate: Mapped[datetime.date] = mapped_column(Date)
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True)
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        onupdate=datetime.datetime.now
    )

    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }