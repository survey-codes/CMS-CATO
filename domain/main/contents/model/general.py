from typing import Optional

from domain.main.menus.entity.menu import Menu


class General:
    pk = property
    image = str
    footer = str
    menu = Optional[Menu]

    def __init__(self, pk: property, image: str, footer: str, menu: Optional[Menu], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.image = image
        self.footer = footer
        self.menu = menu

    def __str__(self):
        return f"{{pk: {self.pk}, image: {self.image}, footer: {self.footer}, menu: {self.menu}}}"
