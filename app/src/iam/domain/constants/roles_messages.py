from app.src.shared.settings import settings


class BaseMessages:
    summary_endpoint_create_role: str
    summary_endpoint_read_role: str
    summary_endpoint_update_role: str
    summary_endpoint_delete_role: str
    generic_error_message: str = "Request failed"
    generic_success_message: str = "Successful request"


class SpanishMessages(BaseMessages):
    summary_endpoint_create_role: str = "Crear un nuevo rol"
    summary_endpoint_read_role: str = "Obtener información de un rol"
    summary_endpoint_update_role: str = "Actualizar un rol existente"
    summary_endpoint_delete_role: str = "Eliminar un rol"


class EnglishMessages(BaseMessages):
    summary_endpoint_create_role: str = "Create a new role"
    summary_endpoint_read_role: str = "Retrieve role information"
    summary_endpoint_update_role: str = "Update an existing role"
    summary_endpoint_delete_role: str = "Delete a role"


def get_messages() -> BaseMessages:
    language = settings.language
    if language.lower() == "es":
        return SpanishMessages()
    elif language.lower() == "en":
        return EnglishMessages()


messages = get_messages()
