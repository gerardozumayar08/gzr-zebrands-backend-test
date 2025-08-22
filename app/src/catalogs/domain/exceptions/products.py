from app.src.shared.domain.exceptions import DomainException
from app.src.catalogs.domain.constants.products_messages import messages

from starlette import status


class CreationProductException(DomainException):
    def __init__(self):
        self.message = messages.create_product_exception_message
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(self.message)


class ProductNotFoundException(DomainException):
    def __init__(self):
        self.message = messages.product_not_found
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(self.message)

