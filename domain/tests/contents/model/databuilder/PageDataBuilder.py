from graphene import ObjectType

from domain.main.contents.model.page import Page


class PageDataBuilder(ObjectType):
    __pk = 1
    __title = "Example"
    __description = "Example"
    __metadata = "{}"
    __children = [1]
    __order = 1
    __slug = "example"

    def with_pk(self, pk: property) -> 'PageDataBuilder':
        self.__pk = pk
        return self

    def with_title(self, title: str) -> 'PageDataBuilder':
        self.__title = title
        return self

    def with_description(self, description: str) -> 'PageDataBuilder':
        self.__description = description
        return self

    def with_slug(self, slug: str) -> 'PageDataBuilder':
        self.__slug = slug
        return self

    def build(self) -> Page:
        return Page(
            self.__pk, self.__title, self.__description, self.__metadata, self.__children, self.__order, self.__slug
        )
