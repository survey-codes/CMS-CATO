from domain.main.exceptions.empty_pk_exception import EmptyPkException
from domain.main.menus.repository.menu_language_repository import MenuLanguageRepository


class MenuLanguageService:
    def __init__(self, menu_language_repository: MenuLanguageRepository):
        self.__menu_language_repository = menu_language_repository

    def select_by_menu_pk(self, menu_pk: property, lang: str):
        if not menu_pk:
            raise EmptyPkException()
        return self.__menu_language_repository.select_by_menu_pk(menu_pk, lang)
