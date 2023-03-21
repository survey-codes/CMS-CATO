from typing import Optional

from domain.main.contents.model.page_language import PageLanguage
from domain.main.contents.repository.page_language_repository import PageLanguageRepository
from domain.main.exceptions.empty_pk_exception import BadPkException


class PageLanguageService:
    def __init__(self, page_language_repository: PageLanguageRepository):
        self.__page_language_repository = page_language_repository

    def select_by_page_pk(self, page_pk: property, lang: str) -> Optional[PageLanguage]:
        if not page_pk:
            raise BadPkException()
        return self.__page_language_repository.select_by_page_pk(page_pk, lang)
