from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

from app.src.iam.domain.permission import Permission
from app.src.iam.domain.role import Role
from app.src.iam.domain.user import User
from app.src.iam.infrastructure.tables.roles_table import role_permissions_table
from app.src.iam.infrastructure.tables.roles_table import roles_table
from app.src.iam.infrastructure.tables.users_table import user_roles_table


def roles_mapper(mapper_registry: registry):
    mapper_registry.map_imperatively(
        Role,
        roles_table,
        properties={
            "permissions": relationship(
                Permission, secondary=role_permissions_table, back_populates="roles"
            ),
            "users": relationship(
                User, secondary=user_roles_table, back_populates="roles"
            ),
        },
    )
