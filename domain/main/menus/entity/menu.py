from domain.main.exceptions.empty_pk_exception import BadPkException
from domain.main.exceptions.empty_value_exception import EmptyValueException
from domain.main.menus.entity.menu_item import MenuItem


class Menu:
    pk = int
    name = str
    metadata = str
    is_general = bool
    items = [MenuItem]

    def __init__(self, pk: property, name: str, metadata: str, is_general: bool, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pk = pk
        self.name = name
        self.metadata = metadata
        self.is_general = is_general
        self.__validations()

    def __validations(self):
        self.__validate_pk()
        self.__validate_name()

    def __validate_pk(self):
        if self.pk < 0:
            raise BadPkException()

    def __validate_name(self):
        if not self.name:
            raise EmptyValueException()
