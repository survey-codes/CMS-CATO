from domain.exceptions.language.empty_abbreviation_exception import EmptyAbbreviationException
from domain.exceptions.language.empty_name_exception import EmptyNameException
from domain.exceptions.language.it_is_not_capitalized_exception import ItIsNotCapitalizedException


class Language:

    def __init__(self, name: str, abbreviation: str):
        self.name = name
        self.abbreviation = abbreviation
        self.__validate_fields()

    def __validate_fields(self):
        self.__name_is_empty()
        self.__abbreviation_is_empty()
        self.__it_is_lowercase()

    def __name_is_empty(self):
        if not self.name:
            raise EmptyNameException()

    def __abbreviation_is_empty(self):
        if not self.abbreviation:
            raise EmptyAbbreviationException()

    def __it_is_lowercase(self):
        if self.abbreviation.islower():
            raise ItIsNotCapitalizedException()
