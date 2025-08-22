from app.src.shared.settings import settings


class BaseMessages:
    user_not_found: str
    invalid_credentials: str
    summary_endpoint_login: str
    generic_error_message: str
    generic_success_message: str
    invalid_token: str
    permission_denied: str


class SpanishMessages(BaseMessages):
    user_not_found = "El usuario no existe"
    invalid_credentials = "Credenciales incorrectas"
    summary_endpoint_login = (
        "Este endpoint permite a un usuario autenticarse con su nombre de usuario y contraseña."
        "Si las credenciales son válidas, se genera y devuelve un token de acceso (por ejemplo, JWT) "
        "que puede ser usado para autenticar futuras solicitudes."
    )
    generic_error_message = "Petición fallida"
    generic_success_message = "Petición exitosa"
    invalid_token = "Token inválido"
    permission_denied = "Permiso denegado"


class EnglishMessages(BaseMessages):
    user_not_found = "The user does not exist."
    invalid_credentials = "Invalid credentials."
    summary_endpoint_login = (
        "This endpoint allows a user to authenticate using their username and password."
        "If the credentials are valid, an access token (e.g., JWT) is generated and returned, "
        "which can be used to authenticate future requests."
    )
    generic_error_message: str = "Request failed"
    generic_success_message: str = "Successful request"
    invalid_token = "Invalid token"
    permission_denied = "Permission denied"


def get_messages() -> BaseMessages:
    language = settings.language
    if language.lower() == "es":
        return SpanishMessages()
    elif language.lower() == "en":
        return EnglishMessages()


messages = get_messages()
