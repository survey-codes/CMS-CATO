from domain.entity.page_language import PageLanguage
from domain.repository.page_language_repository import PageLanguageRepository


class PageLanguageService:
    def __init__(self, page_language_repository: PageLanguageRepository):
        self.__page_language_repository = page_language_repository

    def select(self, lang: str) -> [PageLanguage]:
        return self.__page_language_repository.select(lang)
