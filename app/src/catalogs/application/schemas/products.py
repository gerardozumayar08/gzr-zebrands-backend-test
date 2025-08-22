from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class ProductDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    sku: str
    name: str
    price: float
    brand: str
    # created_by: str
    # modified_by: str
    # created_at: datetime
    # updated_at: datetime


class ProductDTOInput(BaseModel):
    sku: str
    name: str
    price: float
    brand: str


class ProductDTOOptionalInput(BaseModel):
    sku: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
