from domain.repository.general_language_repository import GeneralLanguageRepository
from infrastucture.dataaccess.contents.repository.general_language_repository_imp import GeneralLanguageRepositoryImpl


class GeneralService:
    __general_repository: GeneralLanguageRepository = GeneralLanguageRepositoryImpl()

    def select(self, lang: str):
        return self.__general_repository.select(lang)
