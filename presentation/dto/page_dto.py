from graphene import ObjectType, Int, String, Field

from presentation.dto.menu_dto import MenuDto


class PageDto(ObjectType):
    pk = Int()
    title = String()
    description = String()
    metadata = String()
    order = Int()
    slug = String()
    menu = Field(type=MenuDto)
