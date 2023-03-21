from domain.main.menus.repository.menu_repository import MenuRepository
from infrastucture.dataaccess.menus.acl.menu_acl import MenuAcl
from infrastucture.dataaccess.menus.models.menu import Menu
from infrastucture.dataaccess.menus.models.menu_item import MenuItem


class MenuRepositoryImpl(MenuRepository):
    __menu_acl = MenuAcl()

    def select_by_page_pk(self, page_pk: int, lang: str) -> Menu:
        menu = Menu.objects.filter(page__pk=page_pk).first()
        return self.__menu_acl.from_model_to_domain(menu, lang)
