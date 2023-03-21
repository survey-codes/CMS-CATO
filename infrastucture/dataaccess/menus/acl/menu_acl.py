from typing import Optional

from domain.main.menus.entity.menu import Menu as MenuDomain
from infrastucture.dataaccess.menus.models.menu import Menu as MenuModel


class MenuAcl:

    def from_model_to_domain(self, model: MenuModel, lang: str) -> Optional[MenuDomain]:
        if model:
            language = model.translations.filter(language__abbreviation=lang).first()
            if language:
                name = language.name
                metadata = language.metadata
                return MenuDomain(model.pk, name, metadata, model.is_general)
        return None

    def from_models_to_domains(self, models: [MenuModel]) -> [MenuDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
