from domain.main.contents.repository.general_repository import GeneralRepository
from domain.main.exceptions.language.empty_abbreviation_exception import EmptyAbbreviationException


class GeneralService:

    def __init__(self, general_repository: GeneralRepository):
        self.__general_repository = general_repository

    def select(self, lang: str):
        if not lang:
            raise EmptyAbbreviationException()
        return self.__general_repository.select(lang)
