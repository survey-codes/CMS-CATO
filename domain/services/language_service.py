from domain.entity.language import Language
from domain.repository.language_repository import LanguageRepository
from infrastucture.dataaccess.tools.repository.language_repository_impl import LanguageRepositoryImpl


class LanguageService:
    __language_repository: LanguageRepository = LanguageRepositoryImpl()

    def select(self, abbreviation=None) -> [Language]:
        if abbreviation:
            return self.__language_repository.select_by_abbreviation(abbreviation)
        return self.__language_repository.select()

    def count(self):
        return self.select().count()
