from typing import Any, List, Optional

import factory
from factory import Faker as FFacker
from faker import Faker

from app.src.iam.domain.constants.permissions_enum import PermissionActionsEnum
from app.src.iam.domain.permission import Permission

fake = Faker()


class PermissionsFactory(factory.Factory):
    class Meta:
        model = Permission

    id: Optional[int] = None
    action: str = FFacker("word", ext_word_list=[i.name for i in PermissionActionsEnum])
    resource: str = fake.uri_path()
    roles: Optional[List[Any]] = []

