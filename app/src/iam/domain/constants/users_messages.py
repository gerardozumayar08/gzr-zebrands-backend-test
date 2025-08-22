from app.src.shared.settings import settings


class BaseMessages:
    summary_endpoint_create_user: str
    summary_endpoint_read_user: str
    summary_endpoint_update_user: str
    summary_endpoint_delete_user: str
    create_user_exception_message: str
    generic_error_message: str = "Request failed"
    generic_success_message: str = "Successful request"
    generic_delete_success_message: str = "Deletion was successful"
    


class SpanishMessages(BaseMessages):
    summary_endpoint_create_user: str = "Crear un nuevo usuario"
    summary_endpoint_read_user: str = "Obtener información de un usuario"
    summary_endpoint_update_user: str = "Actualizar un usuario existente"
    summary_endpoint_delete_user: str = "Eliminar un usuario"
    create_user_exception_message: str = "Error al crear el usuario"


class EnglishMessages(BaseMessages):
    summary_endpoint_create_user: str = "Create a new user"
    summary_endpoint_read_user: str = "Retrieve user information"
    summary_endpoint_update_user: str = "Update an existing user"
    summary_endpoint_delete_user: str = "Delete a user"
    create_user_exception_message: str = "Error creating the user"


def get_messages() -> BaseMessages:
    language = settings.language
    if language.lower() == "es":
        return SpanishMessages()
    elif language.lower() == "en":
        return EnglishMessages()


messages = get_messages()
