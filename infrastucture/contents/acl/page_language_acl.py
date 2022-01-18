from typing import Optional

from domain.main.contents.entity.page_language import PageLanguage as PageLanguageDomain
from infrastucture.contents.acl.base_acl import BaseAcl
from infrastucture.contents.models import PageLanguage as PageLanguageModel


class PageLanguageAcl(BaseAcl):
    def from_model_to_domain(self, model: PageLanguageModel) -> Optional[PageLanguageDomain]:
        if not model:
            return None
        return PageLanguageDomain(model.language.abbreviation, model.title, model.description, model.metadata)

    def from_models_to_domains(self, models: [PageLanguageModel]) -> [PageLanguageDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
