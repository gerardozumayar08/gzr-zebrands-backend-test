from dataclasses import dataclass
from typing import List, Optional


from app.src.iam.domain.permission import Permission


@dataclass
class Role:
    name: str
    id: Optional[int] = None
    permissions: Optional[List[Permission]] = None
    users: Optional[List["User"]] = None
