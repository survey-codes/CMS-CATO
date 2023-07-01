from typing import Optional

from domain.main.menus.entity.menu_item import MenuItem as MenuItemDomain
from infrastucture.dataaccess.menus.models.menu_item import MenuItem as MenuItemModel


class MenuItemAcl:
    def from_model_to_domain(self, model: MenuItemModel, lang: str) -> Optional[MenuItemDomain]:
        if model:
            language = model.translations.filter(language__abbreviation=lang).first()
            if language:
                pk = model.pk
                name = language.name
                link = model.link
                sub_item = self.from_model_list_to_domain_list(model.children.all(), lang)
                return MenuItemDomain(pk, name, link, sub_item)
        return None

    def from_model_list_to_domain_list(self, model_list: [MenuItemModel], lang: str) -> [MenuItemDomain]:
        return map(lambda model: self.from_model_to_domain(model, lang), model_list)
