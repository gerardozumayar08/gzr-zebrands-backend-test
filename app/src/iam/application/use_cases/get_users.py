from typing import List, Tuple

from app.src.iam.domain.repositories.users_repository import UsersRepository


class GetUsersUseCase:
    def __init__(self, users_repository: UsersRepository):
        self.users_repository = users_repository

    async def __call__(
        self,
    ) -> Tuple[List[dict], int]:
        data, num_rows = await self.users_repository.get_all()
        return data, num_rows
