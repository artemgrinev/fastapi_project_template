from fastapi import Depends
from src.api_v1.schemas.profile import ProfileUpdate, ProfileCreate
from src.repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository
from src.models.profile import Profile
from config.database.db_helper import db_helper


class ProfileRepositories(SqlAlchemyRepository[ModelType, ProfileCreate, ProfileUpdate]):
    pass

profile_repositories = ProfileRepositories(
    session=db_helper.get_db_session,
    model=Profile
)