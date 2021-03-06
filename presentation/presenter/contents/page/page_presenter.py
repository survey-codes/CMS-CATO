from domain.main.contents.entity.page import Page
from domain.main.contents.repository.page_language_repository import PageLanguageRepository
from domain.main.contents.repository.page_repository import PageRepository
from domain.main.contents.services.page_service import PageService
from domain.main.menus.repository.menu_language_repository import MenuLanguageRepository
from domain.main.menus.repository.menu_repository import MenuRepository
from domain.main.menus.services.menu_service import MenuService
from infrastucture.contents.repository.page_language_repository_impl import PageLanguageRepositoryImpl
from infrastucture.contents.repository.page_repository_impl import PageRepositoryImpl
from infrastucture.menus.repository.menu_language_repository_impl import MenuLanguageRepositoryImpl
from infrastucture.menus.repository.menu_repository_impl import MenuRepositoryImpl


class PagePresenter:
    def __init__(self):
        page_repository: PageRepository = PageRepositoryImpl()
        page_language_repository: PageLanguageRepository = PageLanguageRepositoryImpl()
        self.__page_service = PageService(page_repository, page_language_repository)
        menu_repository: MenuRepository = MenuRepositoryImpl()
        menu_language_repository: MenuLanguageRepository = MenuLanguageRepositoryImpl()
        self.__menu_service = MenuService(menu_repository, menu_language_repository)

    def select(self, lang: str, slug: str) -> [Page]:
        pages = self.__page_service.select(lang, slug)
        return map(lambda page: self.__add_additional_fields(page, lang), pages)

    def __add_additional_fields(self, page: Page, lang: str):
        page.children = self.__page_service.select_children_by_pk(page.pk)
        page.menu = self.__menu_service.select_by_page_pk(page.pk, lang)
        return page
