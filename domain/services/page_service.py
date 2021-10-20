from domain.entity.page import Page
from domain.repository.page_repository import PageRepository


class PageService:
    def __init__(self, page_language_repository: PageRepository):
        self.__page_language_repository = page_language_repository

    def select(self, lang: str, slug: str) -> [Page]:
        return self.__page_language_repository.select(lang, slug)

    def select_children_by_pk(self, pk: property) -> [int]:
        return self.__page_language_repository.select_children_by_pk(pk)
