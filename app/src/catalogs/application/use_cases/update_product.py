from app.src.catalogs.application.schemas.products import (
    ProductDTO,
    ProductDTOOptionalInput,
)
from app.src.catalogs.domain.exceptions.products import (
    CreationProductException,
    ProductNotFoundException,
)
from app.src.catalogs.domain.product import Product
from app.src.catalogs.domain.repositories.products_repository import ProductsRepository
from app.src.shared.domain.bus.publisher_notification_bus import PublishNotificationBus
from app.src.iam.application.use_cases.validate_permissions import (
    ValidatePermissionsUseCase,
)
from app.src.shared.domain.bus.email import EmailSchema
from app.src.shared.settings import settings


class UpdateProductUseCase:
    def __init__(
        self,
        products_repository: ProductsRepository,
        notification_bus: PublishNotificationBus,
        validate_permissions_use_case: ValidatePermissionsUseCase,
    ):
        self.products_repository = products_repository
        self.notification_bus = notification_bus
        self.validate_permissions_use_case = validate_permissions_use_case

    async def __call__(
        self, product_id: int, product_dto: ProductDTOOptionalInput, user_token: str
    ) -> ProductDTO:
        try:
            product = await self.valid_product_exist(product_id)
            user = self.update_product(product, product_dto)
            await self.products_repository.update(user)
            await self.generate_notification(user_token, product_id)
            return ProductDTO.model_validate(user)
        except Exception:
            raise CreationProductException

    async def valid_product_exist(self, user_id):
        user = await self.products_repository.get_by(user_id)
        if not user:
            raise ProductNotFoundException
        return user

    def update_product(
        self, product: Product, product_data_input: ProductDTOOptionalInput
    ):
        product_data_no_none = product_data_input.model_dump(exclude_none=True)
        for key, value in product_data_no_none.items():
            if hasattr(product, key):
                setattr(product, key, value)
        return product

    async def generate_notification(self, token: str, product_id):
        user = await self.validate_permissions_use_case.validate_token(token)

        if user.is_admin():
            admin_users = await self.validate_permissions_use_case.users_repository.get_all_admins()
            emails = [
                EmailSchema(
                    sender=settings.notications_email,
                    destination=user_i.email,
                    subject=f"The user '{user.id}' has updated product '{product_id}'",
                    message=f"The user '{user.id}' has updated product '{product_id}'",
                )
                for user_i in admin_users
                if user_i.id != user.id
            ]
            self.notification_bus.save_mail(emails=emails)
