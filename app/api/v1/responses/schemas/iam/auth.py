from app.api.v1.responses.schemas.generic_response import GenericResponse
from app.src.iam.application.schemas.login import LoginResponse


class LoginSuccessResponse(GenericResponse):
    data: LoginResponse
