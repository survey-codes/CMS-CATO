from graphene import ObjectType, String, Int, List, Field

from domain.entity.menu import Menu
from domain.entity.page_language import PageLanguage
from domain.exceptions.page.empty_title_exception import EmptyTitleException


class Page(ObjectType):
    pk = Int()
    title = String()
    children = List(of_type=Int)
    menu = Field(Menu, id=String())
    order = Int()
    slug = String()
    languages = Field(PageLanguage, id=String())

    def __init__(self, pk: property, title: str, order: int, slug: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.title = title
        self.order = order
        self.slug = slug
        self.__validate_fields()

    def __validate_fields(self):
        self.__is_empty_title()

    def __is_empty_title(self):
        if not self.title:
            raise EmptyTitleException()

    def set_children(self, children: [Int]):
        self.children = children

    def set_languages(self, languages: [PageLanguage]):
        self.languages = languages
