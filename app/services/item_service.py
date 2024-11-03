from typing import Optional

from django.db import transaction

from app.db.models.item import Item
from app.schemas.item import ItemCreate


def create_item(item_data: ItemCreate) -> Item:
    with transaction.atomic():
        item = Item(
            name=item_data.name,
            description=item_data.description,
            price=item_data.price,
            is_available=True,
        )
        item.save()
    return item


def get_item(item_id: int) -> Optional[Item]:
    try:
        return Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return None
