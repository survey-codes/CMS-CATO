from graphene import ObjectType, String, Boolean, Int, Field

from domain.entity.menu_language import MenuLanguage


class Menu(ObjectType):
    pk = Int()
    name = String()
    is_general = Boolean()
    language = Field(MenuLanguage, id=String())

    def __init__(self, pk: property, name: str, is_general: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.name = name
        self.is_general = is_general
