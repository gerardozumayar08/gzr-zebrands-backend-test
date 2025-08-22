from typing import List, Tuple

from app.src.iam.application.schemas.roles import RoleDTO
from app.src.iam.domain.repositories.roles_reporisoty import RolesRepository


class GetRolesUseCase:
    def __init__(self, roles_repository: RolesRepository):
        self.roles_repository = roles_repository

    async def __call__(
        self,
    ) -> Tuple[List[dict], int]:
        rows, num_rows = await self.roles_repository.get_all()
        roles_list = [RoleDTO.model_validate(row) for row in rows]
        return roles_list, num_rows
