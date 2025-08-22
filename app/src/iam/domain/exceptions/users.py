from app.src.shared.domain.exceptions import DomainException
from app.src.iam.domain.constants.users_messages import messages

from starlette import status


class CreationUserException(DomainException):
    def __init__(self):
        self.message = messages.create_user_exception_message
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(self.message)
