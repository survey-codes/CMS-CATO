from domain.main.contents.model.general_language import GeneralDataLanguage as GeneralDataLanguageDomain
from infrastucture.dataaccess.contents.models import GeneralDataLanguage as GeneralDataLanguageModel


class GeneralDataLanguageAcl:
    @staticmethod
    def from_model_to_domain(model: GeneralDataLanguageModel) -> GeneralDataLanguageDomain:
        return GeneralDataLanguageDomain(model.pk, model.footer, model.metadata)

    def from_models_to_domains(self, models: [GeneralDataLanguageModel]) -> [GeneralDataLanguageDomain]:
        return map(lambda model: self.from_model_to_domain(model), models)
