from graphene import ObjectType, Int, String, Field, List

from presentation.dto.post_dto import PostDto
from presentation.dto.section_template_dto import SectionTemplateDto


class SectionDto(ObjectType):
    pk = Int()
    title = String()
    description = String()
    background = String()
    background_color = String()
    template = Field(SectionTemplateDto)
    slug = String()
    order = Int()
    align = String()
    posts = List(PostDto)

