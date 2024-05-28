from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from src.models.user import User
from ..config.auth import current_user
from ..services.profile import profile_crud
from ..schemas.profile import (
    ProfileCreate,
    ProfileResponse,
)


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)

@router.post("/create")
async def create_profile(
        data: ProfileCreate,
        user: User = Depends(current_user),
) -> ProfileResponse:
    data.user_pk = user.id
    print(data)
    try:
        return await profile_crud.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    
    