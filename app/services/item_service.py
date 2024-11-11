from fastapi import HTTPException

from app.db.models import Item
from app.schemas.item_schema import ItemCreateSchema


def create_item(item_data: ItemCreateSchema) -> Item:
    return Item.objects.create(**item_data.model_dump())


def get_item(item_id: int) -> Item:
    try:
        return Item.objects.get(id=item_id)
    except Item.DoesNotExist as err:
        raise HTTPException(status_code=404, detail="Item not found") from err


def update_item(item_id: int, item_data: ItemCreateSchema) -> Item:
    item_obj = get_item(item_id)
    item_obj.name = item_data.name
    item_obj.description = item_data.description
    item_obj.price = item_data.price
    item_obj.save()
    return item_obj


def delete_item(item_id: int) -> None:
    item_obj = get_item(item_id)
    item_obj.delete()
