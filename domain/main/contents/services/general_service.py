from domain.main.contents.repository.general_language_repository import GeneralDataLanguageRepository


class GeneralService:

    def __init__(self, general_language_repository: GeneralDataLanguageRepository):
        self.__general_repository = general_language_repository

    def select(self, lang: str):
        return self.__general_repository.select(lang)
