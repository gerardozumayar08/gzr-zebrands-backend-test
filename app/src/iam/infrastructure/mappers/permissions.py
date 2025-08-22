from sqlalchemy.orm import registry, relationship

from app.src.iam.domain.permission import Permission
from app.src.iam.domain.role import Role
from app.src.iam.infrastructure.tables.permissions_table import permissions_table
from app.src.iam.infrastructure.tables.roles_table import role_permissions_table



def permissions_mapper(mapper_registry: registry):
    mapper_registry.map_imperatively(
        Permission,
        permissions_table,
        properties={
            "roles": relationship(
                Role, secondary=role_permissions_table, back_populates="permissions"
            )
        },
    )
