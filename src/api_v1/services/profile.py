from typing import Optional
from src.api_v1.schemas.profile import ProfileResponse, ProfileUpdate

from src.services.base_services import BaseCRUD
from ..repositories.profile import profile_repositories


class ProfileCRUD(BaseCRUD):
    async def get_profile_by_user_id(self, pk: int, model: ProfileUpdate) -> ProfileResponse | None:
        profile = await self.repository.get_single(user_pk=pk)
        return await self.repository.update(data=model.model_dump(), id=profile.id)

profile_service = ProfileCRUD(repository=profile_repositories)