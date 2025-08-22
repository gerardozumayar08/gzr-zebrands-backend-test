from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Factory

from app.src.catalogs.application.use_cases.create_product import CreateProductUseCase
from app.src.catalogs.application.use_cases.delete_product import DeleteProductUseCase
from app.src.catalogs.application.use_cases.get_products import GetProductsUseCase
from app.src.catalogs.application.use_cases.update_product import UpdateProductUseCase
from app.src.catalogs.infrastructure.repositories.product_views_sqlalchemy_repository import (
    ProductViewsSQLAlchemyRepository,
)
from app.src.catalogs.infrastructure.repositories.products_sqlalchemy_repository import (
    ProductsSQLAlchemyRepository,
)
from app.src.iam.infrastructure.containers.validate_permission_container import (
    ValidatePermissionsContainer,
)
from app.src.shared.infrastructure.containers.main_container import MainContainer


class ProductsContainer(DeclarativeContainer):
    main_container = Container(MainContainer)

    validate_permissions_container = Container(ValidatePermissionsContainer)
    validate_permissions_container.main_container.override(main_container)

    validate_permissions = validate_permissions_container.use_case

    products_sqlalchemy_repository = Factory(
        ProductsSQLAlchemyRepository,
        session=main_container.session,
    )

    product_views_sqlalchemy_repository = Factory(
        ProductViewsSQLAlchemyRepository,
        session=main_container.session,
    )

    get_products = Factory(
        GetProductsUseCase,
        products_repository=products_sqlalchemy_repository,
    )

    create_product = Factory(
        CreateProductUseCase,
        products_repository=products_sqlalchemy_repository,
    )

    update_product = Factory(
        UpdateProductUseCase,
        products_repository=products_sqlalchemy_repository,
        validate_permissions_use_case=validate_permissions,
        notification_bus=main_container.notification_bus,
    )

    delete_product = Factory(
        DeleteProductUseCase,
        products_repository=products_sqlalchemy_repository,
    )
