import datetime
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    last_name: str
    first_name: str
    birthdate: Optional[datetime.date]
    created_at: Optional[datetime.datetime]


class UserCreate(schemas.BaseUserCreate):
    user_name: str
    last_name: str
    first_name: str
    birthdate: Optional[datetime.date]
    created_at: Optional[datetime.datetime]


class UserUpdate(schemas.BaseUserUpdate):
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]