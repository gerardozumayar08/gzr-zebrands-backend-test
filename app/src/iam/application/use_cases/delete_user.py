
from app.src.iam.application.schemas.users import UserDTO
from app.src.iam.domain.exceptions.login import UserNotFoundException
from app.src.iam.domain.repositories.users_repository import UsersRepository


class DeleteUserUseCase:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    async def __call__(
        self, user_id
    ) -> UserDTO:
        user = await self.users_repository.get_by(user_id)
        if not user:
            raise UserNotFoundException
        await self.users_repository.delete(user)
