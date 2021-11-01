from typing import Optional

from domain.entity.menu import Menu
from domain.exceptions.empty_pk_exception import EmptyPkException
from domain.repository.menu_language_repository import MenuLanguageRepository
from domain.repository.menu_repository import MenuRepository
from domain.services.menu_language_service import MenuLanguageService


class MenuService:

    def __init__(self, menu_repository: MenuRepository, menu_language_repository: MenuLanguageRepository):
        self.__menu_repository = menu_repository
        self.__menu_language_service = MenuLanguageService(menu_language_repository)

    def select_by_page_pk(self, page_pk: int, lang: str) -> Optional[Menu]:
        if not page_pk:
            raise EmptyPkException()
        menu = self.__menu_repository.select_by_page_pk(page_pk)
        if menu:
            return self.__add_language(menu, lang)
        return None

    def __add_language(self, menu: Menu, lang: str) -> Menu:
        language = self.__menu_language_service.select_by_menu_pk(menu.pk, lang)
        if language:
            menu.name = language.name
            menu.metadata = language.metadata
        return menu
