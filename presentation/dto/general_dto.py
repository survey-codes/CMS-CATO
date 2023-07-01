from graphene import ObjectType, Int, String, JSONString, Field

from presentation.dto.menu_dto import MenuDto


class GeneralDto(ObjectType):
    pk = Int()
    image = String()
    footer = String()
    metadata = JSONString()
    menu = Field(type=MenuDto)
