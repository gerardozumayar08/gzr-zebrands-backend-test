from typing import List

from app.api.v1.responses.schemas.generic_response import GenericResponse
from app.src.iam.application.schemas.users import UserDTO


class GetUsersSuccessResponse(GenericResponse):
    data: List[UserDTO]


class CreateUserSuccessResponse(GenericResponse):
    data: UserDTO


class UpdateUserSuccessResponse(CreateUserSuccessResponse): ...
