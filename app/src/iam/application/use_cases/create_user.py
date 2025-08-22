from typing import List, Tuple

from app.src.iam.domain.repositories.users_repository import UsersRepository
from app.src.iam.domain.repositories.roles_reporisoty import RolesRepository
from app.src.iam.application.schemas.users import UserDTOInput, UserDTO
from app.src.iam.domain.user import User
from app.src.iam.domain.exceptions.users import CreationUserException
from app.src.iam.infrastructure.auth import hash_password


class CreateUserUseCase:
    def __init__(
        self, users_repository: UsersRepository, roles_repository: RolesRepository
    ):
        self.users_repository = users_repository
        self.roles_repository = roles_repository

    async def __call__(self, user_dto: UserDTOInput) -> Tuple[List[dict], int]:
        try:
            hashed_pass = hash_password(user_dto.password)
            user = User(
                **user_dto.model_dump(exclude={"roles_ids", "password"}),
                is_active=True,
                hashed_password=hashed_pass,
            )
            roles = [
                await self.roles_repository.get_by(role_id)
                for role_id in user_dto.roles_ids
            ]
            user.roles = roles
            user.is_active = True
            await self.users_repository.save(user)
            return UserDTO.model_validate(user)
        except Exception:
            raise CreationUserException
