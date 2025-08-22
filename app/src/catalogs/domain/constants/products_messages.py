from app.src.shared.settings import settings


class BaseMessages:
    summary_endpoint_create_product: str
    summary_endpoint_read_product: str
    summary_endpoint_update_product: str
    summary_endpoint_delete_product: str
    create_product_exception_message: str
    product_not_found: str = "Product not found"
    generic_error_message: str = "Request failed"
    generic_success_message: str = "Successful request"
    generic_delete_success_message: str = "Deletion was successful"
    


class SpanishMessages(BaseMessages):
    summary_endpoint_create_product: str = "Crear un nuevo producto"
    summary_endpoint_read_product: str = "Obtener información de un producto"
    summary_endpoint_update_product: str = "Actualizar un producto existente"
    summary_endpoint_delete_product: str = "Eliminar un producto"
    create_product_exception_message: str = "Error al crear el producto"


class EnglishMessages(BaseMessages):
    summary_endpoint_create_product: str = "Create a new product"
    summary_endpoint_read_product: str = "Retrieve product information"
    summary_endpoint_update_product: str = "Update an existing product"
    summary_endpoint_delete_product: str = "Delete a product"
    create_product_exception_message: str = "Error creating the product"


def get_messages() -> BaseMessages:
    language = settings.language
    if language.lower() == "es":
        return SpanishMessages()
    elif language.lower() == "en":
        return EnglishMessages()


messages = get_messages()
