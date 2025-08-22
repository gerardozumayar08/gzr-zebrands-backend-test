from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

from app.src.iam.domain.role import Role
from app.src.iam.domain.user import User
from app.src.iam.infrastructure.tables.users_table import user_roles_table
from app.src.iam.infrastructure.tables.users_table import users_table


def users_mapper(mapper_registry: registry):
    mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "roles": relationship(
                Role, secondary=user_roles_table, back_populates="users"
            )
        },
    )
