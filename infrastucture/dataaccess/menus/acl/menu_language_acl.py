from typing import Optional

from domain.entity.menu_language import MenuLanguage as MenuLanguageDomain
from infrastucture.dataaccess.contents.acl.base_acl import BaseAcl
from infrastucture.dataaccess.menus.models.menu_language import MenuLanguage as MenuLanguageModel


class MenuLanguageAcl(BaseAcl):
    def from_model_to_domain(self, model: MenuLanguageModel) -> Optional[MenuLanguageDomain]:
        if not model:
            return None
        return MenuLanguageDomain(model.language.name, model.name, model.metadata)

    def from_models_to_domains(self, models: [MenuLanguageModel]) -> [MenuLanguageDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
