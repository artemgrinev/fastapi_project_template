from src.services.base_services import BaseCRUD
from ..repositories.profile import profile_repositories


class ProfileCRUD(BaseCRUD):
    pass

profile_crud = ProfileCRUD(repository=profile_repositories)