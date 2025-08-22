from app.src.iam.application.schemas.users import UserDTO, UserDTOOptionalInput
from app.src.iam.domain.exceptions.login import UserNotFoundException
from app.src.iam.domain.exceptions.users import CreationUserException
from app.src.iam.domain.repositories.roles_reporisoty import RolesRepository
from app.src.iam.domain.repositories.users_repository import UsersRepository
from app.src.iam.domain.user import User
from app.src.iam.infrastructure.auth import hash_password


class UpdateUserUseCase:
    def __init__(
        self, users_repository: UsersRepository, roles_repository: RolesRepository
    ):
        self.users_repository = users_repository
        self.roles_repository = roles_repository

    async def __call__(self, user_id: int, user_dto: UserDTOOptionalInput) -> UserDTO:
        try:
            user = await self.valid_user_exist(user_id)
            user = await self.update_user(user, user_dto)
            await self.users_repository.update(user)
            return UserDTO.model_validate(user)
        except Exception:
            raise CreationUserException

    async def valid_user_exist(self, user_id):
        user = await self.users_repository.get_by(user_id)
        if not user:
            raise UserNotFoundException
        return user

    async def update_user(self, user: User, user_data_input: UserDTOOptionalInput):
        user_data_no_none = user_data_input.model_dump(exclude_none=True)
        for key, value in user_data_no_none.items():
            if hasattr(user, key):
                setattr(user, key, value)

            if key == "password":
                user.hashed_password = hash_password(user_data_input.password)

            if key == "roles_ids" and user_data_input.roles_ids:
                roles = [
                    await self.roles_repository.get_by(role_id)
                    for role_id in user_data_input.roles_ids
                ]
                user.roles = roles
        return user
