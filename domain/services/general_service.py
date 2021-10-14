from domain.repository.general_language_repository import GeneralLanguageRepository


class GeneralService:

    def __init__(self, general_language_repository: GeneralLanguageRepository):
        self.__general_repository = general_language_repository

    def select(self, lang: str):
        return self.__general_repository.select(lang)
