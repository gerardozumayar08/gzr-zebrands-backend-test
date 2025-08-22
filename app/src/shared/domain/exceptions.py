from app.src.shared.message_constants import messages


class DomainException(Exception):
    def __init__(self, message: str):
        self.message = message


class AsyncHTTPClientException(DomainException):
    def __init__(self, message):
        self.message = messages.async_http_client_exception_message.format(message)
        super().__init__(self.message)
