from domain.main.tools.entity.language import Language as LanguageDomain
from infrastucture.tools.models import Language as LanguageModel


class LanguageAcl:
    @staticmethod
    def from_model_to_domain(model) -> LanguageDomain:
        return LanguageDomain(model.name, model.abbreviation)

    def from_list_model_to_list_domain(self, models: [LanguageModel]) -> [LanguageDomain]:
        languages: [LanguageDomain] = []
        for language in models:
            domain = self.from_model_to_domain(language)
            languages.append(domain)
        return languages
