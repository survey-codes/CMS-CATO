from django.db.models import QuerySet

from domain.entity.language import Language as LanguageDomain


class LanguageAcl:
    @staticmethod
    def from_model_to_domain(model) -> LanguageDomain:
        return LanguageDomain(model.name, model.abbreviation)

    def from_list_model_to_list_domain(self, models: QuerySet) -> [LanguageDomain]:
        languages: [LanguageDomain] = []
        for language in models:
            domain = self.from_model_to_domain(language)
            languages.append(domain)
        assert languages, "Lo sentimos :( no encontramos un idiomas"
        return languages
