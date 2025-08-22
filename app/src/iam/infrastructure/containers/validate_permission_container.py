from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Factory

from app.src.iam.application.use_cases.validate_permissions import (
    ValidatePermissionsUseCase,
)
from app.src.iam.infrastructure.repositories.users_sqlalchemy_repository import (
    UsersSQLAlchemyRepository,
)
from app.src.shared.infrastructure.containers.main_container import MainContainer


class ValidatePermissionsContainer(DeclarativeContainer):
    main_container = Container(MainContainer)

    users_sqlalchemy_repository = Factory(
        UsersSQLAlchemyRepository,
        session=main_container.session,
    )

    use_case = Factory(
        ValidatePermissionsUseCase,
        users_repository=users_sqlalchemy_repository,
    )
