from domain.entity.general_language import GeneralLanguage
from domain.repository.general_language_repository import GeneralLanguageRepository


class GeneralLanguageRepositoryImpl(GeneralLanguageRepository):
    def select(self, lang: str) -> [GeneralLanguage]:
        return [GeneralLanguage("Algo", "{algo:algo}"), ]
