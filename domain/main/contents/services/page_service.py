from domain.main.contents.model.page import Page
from domain.main.contents.repository.page_language_repository import PageLanguageRepository
from domain.main.contents.repository.page_repository import PageRepository
from domain.main.contents.services.page_language_service import PageLanguageService


class PageService:

    def __init__(self, page_repository: PageRepository, page_language_repository: PageLanguageRepository):
        self.__page_repository = page_repository
        self.__page_language_service = PageLanguageService(page_language_repository)

    def select(self, lang: str, slug: str) -> [Page]:
        return self.__page_repository.select(lang, slug)

    def select_children_by_pk(self, pk: property) -> [int]:
        return self.__page_repository.select_children_by_pk(pk)
