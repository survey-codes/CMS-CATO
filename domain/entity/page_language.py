from graphene import ObjectType, String, JSONString, Int

from domain.main.exceptions.empty_value_exception import EmptyValueException


class PageLanguage(ObjectType):
    pk = Int()
    title = String()
    description = String()
    metadata = JSONString()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__validate_fields()

    def __validate_fields(self):
        self.__is_empty_title()

    def __is_empty_title(self):
        if not self.title:
            raise EmptyValueException()
