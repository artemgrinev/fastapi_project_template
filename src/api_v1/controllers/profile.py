from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from src.models.user import User
from ..config.auth import current_user
from ..services.profile import profile_service
from ..schemas.profile import (
    ProfileCreate,
    ProfileResponse,
    ProfileUpdate,
)


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("/{id}")
async def get_profile_by_id(id: int) -> ProfileResponse:
    try:
        return await profile_service.get(pk=id)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    

@router.post("/create")
async def create_profile(
        data: ProfileCreate,
        user: User = Depends(current_user),
) -> ProfileResponse:
    data.user_pk = user.id
    try:
        return await profile_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    

@router.put("/update")
async def update_profile(
        data: ProfileUpdate,
        user: User = Depends(current_user),
) -> ProfileResponse:
    user_id = user.id
    try:
        return await profile_service.get_profile_by_user_id(pk=user_id, model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))