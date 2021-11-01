from domain.entity.page import Page
from domain.repository.page_language_repository import PageLanguageRepository
from domain.repository.page_repository import PageRepository
from domain.services.page_language_service import PageLanguageService


class PageService:

    def __init__(self, page_repository: PageRepository, page_language_repository: PageLanguageRepository):
        self.__page_repository = page_repository
        self.__page_language_service = PageLanguageService(page_language_repository)

    def select(self, lang: str, slug: str) -> [Page]:
        pages = self.__page_repository.select(lang, slug)
        return map(lambda page: self.__add_language(page, lang), pages)

    def __add_language(self, page: Page, lang: str) -> Page:
        language = self.__page_language_service.select_by_page_pk(page.pk, lang)
        if language:
            page.title = language.title
            page.description = language.description
            page.metadata = language.metadata
        return page

    def select_children_by_pk(self, pk: property) -> [int]:
        return self.__page_repository.select_children_by_pk(pk)
