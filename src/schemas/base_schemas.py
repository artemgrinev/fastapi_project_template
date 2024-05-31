from typing import NewType

from pydantic import BaseModel, Field

PyModel = NewType("PyModel", BaseModel)


class Base(BaseModel):
    class Config:
        from_attributes = True


class ID(BaseModel):
    id: int = Field(ge=1, le=999999)