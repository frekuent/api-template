from pydantic import BaseModel


class ItemCreateSchema(BaseModel):
    name: str
    description: str
    price: float


class ItemResponseSchema(ItemCreateSchema):
    id: int
    is_available: bool

    class Config:
        orm_mode = True
