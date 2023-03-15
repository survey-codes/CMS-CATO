from typing import Optional

from domain.main.menus.entity.menu import Menu as MenuDomain
from infrastucture.contents.acl.base_acl import BaseAcl
from infrastucture.menus.models.menu import Menu as MenuModel


class MenuAcl(BaseAcl):

    def from_model_to_domain(self, model: MenuModel) -> Optional[MenuDomain]:
        if model:
            return MenuDomain(model.pk, model.name, model.is_general)
        else:
            return None

    def from_models_to_domains(self, models: [MenuModel]) -> [MenuDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
