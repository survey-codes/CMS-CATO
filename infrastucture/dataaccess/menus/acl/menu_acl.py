from typing import Optional

from domain.main.menus.entity.menu import Menu as MenuDomain
from infrastucture.dataaccess.menus.acl.menu_item_acl import MenuItemAcl
from infrastucture.dataaccess.menus.models.menu import Menu as MenuModel


class MenuAcl:
    __menu_item_acl = MenuItemAcl()

    def from_model_to_domain(self, model: MenuModel, lang: str) -> Optional[MenuDomain]:
        if model:
            language = model.translations.filter(language__abbreviation=lang).first()
            if language:
                items = self.__menu_item_acl.from_model_list_to_domain_list(model.items.all(), lang)
                name = language.name
                metadata = language.metadata
                return MenuDomain(model.pk, name, metadata, model.is_general, items)
        return None

    def from_models_to_domains(self, models: [MenuModel], lang: str) -> [MenuDomain]:
        return map(lambda model: self.from_model_to_domain(model, lang), models)
