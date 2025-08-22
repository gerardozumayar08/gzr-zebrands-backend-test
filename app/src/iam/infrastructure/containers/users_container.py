from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Container, Factory

from app.src.iam.application.use_cases.create_user import CreateUserUseCase
from app.src.iam.application.use_cases.delete_user import DeleteUserUseCase
from app.src.iam.application.use_cases.get_users import GetUsersUseCase
from app.src.iam.application.use_cases.update_user import UpdateUserUseCase
from app.src.iam.infrastructure.containers.validate_permission_container import (
    ValidatePermissionsContainer,
)
from app.src.iam.infrastructure.repositories.roles_sqlalchemy_repository import (
    RolesSQLAlchemyRepository,
)
from app.src.iam.infrastructure.repositories.users_sqlalchemy_repository import (
    UsersSQLAlchemyRepository,
)
from app.src.shared.infrastructure.containers.main_container import MainContainer


class UsersContainer(DeclarativeContainer):
    main_container = Container(MainContainer)

    validate_permissions_container = Container(ValidatePermissionsContainer)
    validate_permissions_container.main_container.override(main_container)

    validate_permissions = validate_permissions_container.use_case

    users_sqlalchemy_repository = Factory(
        UsersSQLAlchemyRepository,
        session=main_container.session,
    )

    roles_sqlalchemy_repository = Factory(
        RolesSQLAlchemyRepository,
        session=main_container.session,
    )

    get_users = Factory(
        GetUsersUseCase,
        users_repository=users_sqlalchemy_repository,
    )

    create_user = Factory(
        CreateUserUseCase,
        users_repository=users_sqlalchemy_repository,
        roles_repository=roles_sqlalchemy_repository,
    )

    update_user = Factory(
        UpdateUserUseCase,
        users_repository=users_sqlalchemy_repository,
        roles_repository=roles_sqlalchemy_repository,
    )

    delete_user = Factory(
        DeleteUserUseCase,
        users_repository=users_sqlalchemy_repository,
    )
