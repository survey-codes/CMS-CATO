from typing import Optional

from domain.entity.menu import Menu as MenuDomain
from infrastucture.dataaccess.menus.models.menu import Menu as MenuModel


class MenuAcl:
    @staticmethod
    def from_model_to_domain(model: MenuModel) -> Optional[MenuDomain]:
        if model:
            return MenuDomain(model.pk, model.is_general)
        else:
            return None
