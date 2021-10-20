from domain.entity.page import Page
from domain.repository.menu_repository import MenuRepository
from domain.repository.page_language_repository import PageLanguageRepository
from domain.repository.page_repository import PageRepository
from domain.services.menu_service import MenuService
from domain.services.page_language_service import PageLanguageService
from domain.services.page_service import PageService
from infrastucture.dataaccess.contents.repository.page_language_repository_impl import PageLanguageRepositoryImpl
from infrastucture.dataaccess.contents.repository.page_repository_impl import PageRepositoryImpl
from infrastucture.dataaccess.menus.repository.menu_repository_impl import MenuRepositoryImpl


class PagePresenter:
    def __init__(self):
        page_repository: PageRepository = PageRepositoryImpl()
        self.__page_service = PageService(page_repository)
        menu_repository: MenuRepository = MenuRepositoryImpl()
        self.__menu_service = MenuService(menu_repository)
        page_language_repository: PageLanguageRepository = PageLanguageRepositoryImpl()
        self.__page_language_service = PageLanguageService(page_language_repository)

    def select(self, lang: str, slug: str) -> [Page]:
        pages = self.__page_service.select(lang, slug)
        return map(lambda page: self.__add_additional_fields(page, lang), pages)

    def __add_additional_fields(self, page: Page, lang: str):
        page.children = self.__page_service.select_children_by_pk(page.pk)
        page.menu = self.__menu_service.select_by_page_pk(page.pk)
        page.languages = self.__page_language_service.select_by_page_pk(page.pk, lang)
        return page
