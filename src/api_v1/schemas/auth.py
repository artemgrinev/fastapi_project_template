import datetime
from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    user_name: str

class UserCreate(schemas.BaseUserCreate):
    user_name: str

class UserUpdate(schemas.BaseUserUpdate):
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
