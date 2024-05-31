import datetime
from typing import Optional
from pydantic import BaseModel


class ProfileResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]

class ProfileCreate(BaseModel):
    user_pk: int
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]
    
class ProfileUpdate(BaseModel):
    first_name: str
    last_name: str
    birthdate: Optional[datetime.date]

class ProfileDelete(BaseModel):
    id: int
    user_id: int
    is_active: Optional[bool] = False

class HTTP_404(BaseModel):
    detail: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "detail": "Profile not found",
                },
            ]
        }
    }


class HTTP_422(BaseModel):
    detail: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "detail": "Input must be a valid integer not exceeding 10 characters",
                },
            ]
        }
    }