from domain.entity.page_language import PageLanguage as PageLanguageDomain
from infrastucture.dataaccess.contents.models import PageLanguage as PageLanguageModel


class PageLanguageAcl:
    @staticmethod
    def from_model_to_domain(model: PageLanguageModel) -> PageLanguageDomain:
        return PageLanguageDomain(model.pk, model.title, model.description, model.metadata)

    def from_models_to_domains(self, models: [PageLanguageModel]) -> [PageLanguageDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
