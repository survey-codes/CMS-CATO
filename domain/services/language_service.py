from domain.entity.language import Language
from domain.repository.language_repository import LanguageRepository


class LanguageService:

    def __init__(self, language_repository: LanguageRepository):
        self.__language_repository = language_repository

    def select(self, abbreviation=None) -> [Language]:
        if abbreviation:
            return self.__language_repository.select_by_abbreviation(abbreviation)
        return self.__language_repository.select()

    def count(self):
        return self.select().count()
