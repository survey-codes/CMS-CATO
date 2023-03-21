from typing import Optional

from graphene import Int

from domain.main.exceptions.empty_pk_exception import BadPkException
from domain.main.exceptions.empty_value_exception import EmptyValueException
from domain.main.menus.entity.menu import Menu


class Page:
    pk = property
    title = str
    description = str
    metadata = str
    children = [int]
    order = int
    slug = str
    menu = Optional[Menu]

    def __init__(
        self,
        pk: property,
        title: str,
        description: str,
        metadata: str,
        children: [int],
        order: int,
        slug: str,
        menu: Optional[Menu],
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.title = title
        self.description = description
        self.metadata = metadata
        self.children = children
        self.order = order
        self.slug = slug
        self.menu = menu
        self.__validation()

    def __validation(self):
        self.__validate_pk()
        self.__validate_title()
        self.__validate_slug()

    def __validate_pk(self):
        if self.pk < 0:
            raise BadPkException()

    def __validate_title(self):
        if not self.title:
            raise EmptyValueException()

    def __validate_description(self):
        if not self.description:
            raise EmptyValueException()

    def __validate_slug(self):
        if not self.slug:
            raise EmptyValueException()

    def set_children(self, children: [Int]):
        self.children = children
