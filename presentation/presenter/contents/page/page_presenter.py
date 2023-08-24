from domain.main.contents.model.page import Page
from domain.main.contents.repository.page_language_repository import PageLanguageRepository
from domain.main.contents.repository.page_repository import PageRepository
from domain.main.contents.services.page_service import PageService
from infrastucture.dataaccess.contents.repository.page_language_repository_impl import PageLanguageRepositoryImpl
from infrastucture.dataaccess.contents.repository.page_repository_impl import PageRepositoryImpl


class PagePresenter:
    def __init__(self):
        page_repository: PageRepository = PageRepositoryImpl()
        page_language_repository: PageLanguageRepository = PageLanguageRepositoryImpl()
        self.__page_service = PageService(page_repository, page_language_repository)

    def select(self, lang: str, slug: str) -> [Page]:
        pages = self.__page_service.select(lang, slug)
        return pages
