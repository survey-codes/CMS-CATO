from typing import Optional

from domain.entity.menu import Menu
from domain.exceptions.empty_pk_exception import EmptyPkException
from domain.repository.menu_repository import MenuRepository


class MenuService:

    def __init__(self, menu_repository: MenuRepository):
        self.__menu_repository = menu_repository

    def select_by_page_pk(self, page_pk: int) -> Optional[Menu]:
        if not page_pk:
            raise EmptyPkException()
        return self.__menu_repository.select_by_page_pk(page_pk)
