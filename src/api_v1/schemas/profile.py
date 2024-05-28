import datetime
from typing import Optional
from pydantic import BaseModel

class BaseProfile(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]

class ProfileCreate(BaseProfile):
    user_pk: int

class ProfileResponse(BaseProfile):
    id: int
    
class ProfileUpdate(BaseProfile):
    id: int

class ProfileDelete(BaseModel):
    id: int
    user_id: int
    is_active: Optional[bool] = False