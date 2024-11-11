from fastapi import APIRouter

from app.schemas.item_schema import ItemCreateSchema, ItemResponseSchema
from app.services.item_service import create_item, delete_item, get_item, update_item

router = APIRouter()


@router.post("/", response_model=ItemResponseSchema)
def create_item_route(item: ItemCreateSchema):
    return create_item(item)


@router.get("/{item_id}", response_model=ItemResponseSchema)
def get_item_route(item_id: int):
    return get_item(item_id)


@router.put("/{item_id}", response_model=ItemResponseSchema)
def update_item_route(item_id: int, item: ItemCreateSchema):
    return update_item(item_id, item)


@router.delete("/{item_id}")
def delete_item_route(item_id: int):
    delete_item(item_id)
    return {"detail": "Item deleted"}
