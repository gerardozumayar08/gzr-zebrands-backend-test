import pytest
from sqlalchemy.orm import Session

from app.src.iam.domain.user import User
from app.src.iam.domain.role import Role
from app.src.iam.domain.permission import Permission
from tests.factories.domain.iam.users_factory import UsersFactory
from tests.factories.domain.iam.permissions_factory import PermissionsFactory
from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from tests.factories.domain.iam.roles_factory import RolesFactory
from app.src.iam.infrastructure.auth import hash_password


@pytest.fixture
async def data_users(
    main_container_uow,
):
    session: Session = main_container_uow.session

    anonymous_perms = [
        PermissionsFactory(resource="/catalogs/products", action=PermissionActionsEnum.read),
    ]

    admin_perms = [
        PermissionsFactory(resource="/admin/users", action=PermissionActionsEnum.create),
        PermissionsFactory(resource="/admin/users", action=PermissionActionsEnum.update),
        PermissionsFactory(resource="/admin/users", action=PermissionActionsEnum.delete),
        PermissionsFactory(resource="/admin/users", action=PermissionActionsEnum.read),

        PermissionsFactory(resource="/admin/roles", action=PermissionActionsEnum.create),
        PermissionsFactory(resource="/admin/roles", action=PermissionActionsEnum.update),
        PermissionsFactory(resource="/admin/roles", action=PermissionActionsEnum.delete),
        PermissionsFactory(resource="/admin/roles", action=PermissionActionsEnum.read),

        PermissionsFactory(resource="/catalogs/products", action=PermissionActionsEnum.create),
        PermissionsFactory(resource="/catalogs/products", action=PermissionActionsEnum.update),
        PermissionsFactory(resource="/catalogs/products", action=PermissionActionsEnum.delete),
        *anonymous_perms
    ]

    
    session.add_all(admin_perms)
    session.flush()

    admin_role = RolesFactory(name="admin")
    anonymous_role = RolesFactory(name="anonymous")
    admin_role.permissions = admin_perms  
    anonymous_role.permissions = anonymous_perms

    session.add(admin_role)
    session.add(anonymous_role)
    session.flush()

    admin_user = UsersFactory(
        username="admin",
        fullname="Full Name Admin",
        email="admin@example.com",
        hashed_password=hash_password("admin123"),
    )

    anonymous_user = UsersFactory(
        username="anonymous",
        fullname="Full Name Anonymous",
        email="anonymous@example.com",
        hashed_password=hash_password("anonymous123"),
    )
    admin_user.roles = [admin_role]
    anonymous_user.roles = [anonymous_role]

    session.add(admin_user)
    session.add(anonymous_user)
    await main_container_uow.commit()


@pytest.mark.asyncio
async def test_users(data_users, main_container_uow):
    permission_db = main_container_uow.session.query(Permission).all()
    assert permission_db
