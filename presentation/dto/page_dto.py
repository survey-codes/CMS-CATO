from graphene import ObjectType, Int, String, Field, List

from presentation.dto.menu_dto import MenuDto
from presentation.dto.section_dto import SectionDto


class PageDto(ObjectType):
    pk = Int()
    title = String()
    description = String()
    metadata = String()
    order = Int()
    slug = String()
    menu = Field(type=MenuDto)
    sections = List(SectionDto)
