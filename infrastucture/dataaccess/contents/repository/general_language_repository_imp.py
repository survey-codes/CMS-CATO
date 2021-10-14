from domain.entity.general_language import GeneralLanguage
from domain.repository.general_language_repository import GeneralLanguageRepository


class GeneralLanguageRepositoryImpl(GeneralLanguageRepository):
    def select(self, lang: str) -> [GeneralLanguage]:
        assert lang == "ES", "No tenemos nada con este idioma"
        return [GeneralLanguage("Algo", "{algo:algo}"), ]