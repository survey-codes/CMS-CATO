from graphene import ObjectType, String, Boolean, Int, Field

from domain.entity.menu_language import MenuLanguage


class Menu(ObjectType):
    pk = Int()
    name = String()
    metadata = String()
    is_general = Boolean()

    def __init__(self, pk: property, is_general: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.is_general = is_general
