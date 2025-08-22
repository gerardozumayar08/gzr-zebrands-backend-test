from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Factory

from app.src.iam.application.use_cases.get_roles import GetRolesUseCase
from app.src.iam.infrastructure.containers.validate_permission_container import (
    ValidatePermissionsContainer,
)
from app.src.iam.infrastructure.repositories.roles_sqlalchemy_repository import (
    RolesSQLAlchemyRepository,
)
from app.src.shared.infrastructure.containers.main_container import MainContainer


class RolesContainer(DeclarativeContainer):
    main_container = Container(MainContainer)

    validate_permissions_container = Container(ValidatePermissionsContainer)
    validate_permissions_container.main_container.override(main_container)

    validate_permissions = validate_permissions_container.use_case

    roles_sqlalchemy_repository = Factory(
        RolesSQLAlchemyRepository,
        session=main_container.session,
    )

    get_roles= Factory(
        GetRolesUseCase,
        roles_repository=roles_sqlalchemy_repository,
    )
