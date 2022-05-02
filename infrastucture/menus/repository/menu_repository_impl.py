from domain.main.menus.repository.menu_repository import MenuRepository
from infrastucture.menus.acl.menu_acl import MenuAcl
from infrastucture.menus.models.menu import Menu


class MenuRepositoryImpl(MenuRepository):
    __menu_acl = MenuAcl()

    def select_by_page_pk(self, page_pk: int) -> Menu:
        menu = Menu.objects.filter(page__pk=page_pk).first()
        return self.__menu_acl.from_model_to_domain(menu)
