from app.src.shared.settings import settings


class BaseMessages:
    async_http_client_exception_message: str


class SpanishMessages(BaseMessages):
    async_http_client_exception_message = (
        "Un error ocurrió mientras se hacía la petición: {message}"
    )


class EnglishMessages(BaseMessages):
    async_http_client_exception_message = (
        "An error occurred while making the request: {message}"
    )


def get_messages() -> BaseMessages:
    language = settings.language
    if language == "es":
        return SpanishMessages()
    else:
        return EnglishMessages()
    
messages = get_messages()
