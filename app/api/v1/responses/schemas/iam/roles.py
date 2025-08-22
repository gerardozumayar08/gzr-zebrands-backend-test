from typing import List

from app.api.v1.responses.schemas.generic_response import GenericResponse
from app.src.iam.application.schemas.roles import RoleDTO


class GetRolesSuccessResponse(GenericResponse):
    data: List[RoleDTO]
