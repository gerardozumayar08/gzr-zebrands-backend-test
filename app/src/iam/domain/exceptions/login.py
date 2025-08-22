from app.src.shared.domain.exceptions import DomainException
from app.src.iam.domain.constants.login_messages import messages

from starlette import status


class UserNotFoundException(DomainException):
    def __init__(self):
        self.message = messages.user_not_found
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(self.message)


class InvalidaCredentialsException(DomainException):
    def __init__(self):
        self.message = messages.invalid_credentials
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(self.message)


class InvalidaTokenException(DomainException):
    def __init__(self):
        self.message = messages.invalid_token
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(self.message)


class PermissionDeniedException(DomainException):
    def __init__(self):
        self.message = messages.permission_denied
        self.status_code = status.HTTP_403_FORBIDDEN
        super().__init__(self.message)
