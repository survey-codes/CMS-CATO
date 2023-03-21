from graphene import ObjectType, Int, String, Boolean, List

from presentation.dto.menu_item_dto import MenuItemDto


class MenuDto(ObjectType):
    pk = Int()
    name = String()
    metadata = String()
    is_general = Boolean()
    items = List(MenuItemDto)
