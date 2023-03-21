from graphene import ObjectType, String, Int, List


class MenuItemDto(ObjectType):
    pk = Int()
    name = String()
    link = String()
    sub_item = List(lambda: MenuItemDto)
