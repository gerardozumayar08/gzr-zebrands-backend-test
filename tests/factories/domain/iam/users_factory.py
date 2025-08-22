from typing import Any, List, Optional

import factory
from faker import Faker

from app.src.iam.domain.user import User

fake = Faker()


class UsersFactory(factory.Factory):
    class Meta:
        model = User

    id: Optional[int] = None
    username: str = fake.user_name()
    fullname: str = fake.name()
    email: str = fake.email()
    hashed_password: str = fake.uuid4()
    is_active: bool = True
    roles: Optional[List[Any]] = []
