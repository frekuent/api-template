from decimal import Decimal

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: str
    price: Decimal


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
    is_available: bool

    class Config:
        from_attributes = True
