from graphene import ObjectType, String, Int, List, Field, JSONString

from domain.main.contents.entity.section import Section
from domain.main.menus.entity.menu import Menu


class Page(ObjectType):
    pk = Int()
    title = String()
    description = String()
    metadata = JSONString()
    children = List(of_type=Int)
    menu = Field(Menu, id=String())
    order = Int()
    slug = String()
    sections = List(of_type=Section)

    def __init__(self, pk: property, order: int, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.order = order
        self.slug = slug

    def set_children(self, children: [Int]):
        self.children = children
