from typing import Any, List, Optional

import factory
from faker import Faker

from app.src.iam.domain.role import Role

fake = Faker()


class RolesFactory(factory.Factory):
    class Meta:
        model = Role

    id: Optional[int] = None
    name: str = fake.name()
    permissions: Optional[List[Any]] = []
    users: Optional[List[Any]] = []
