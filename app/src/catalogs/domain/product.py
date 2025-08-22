from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    sku: str
    name: str
    price: float
    brand: str
    id: Optional[int] = None
    