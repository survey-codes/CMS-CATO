from domain.entity.page_language import PageLanguage
from domain.repository.page_language_repository import PageLanguageRepository


class PageLanguageRepositoryImpl(PageLanguageRepository):
    def select(self, lang: str) -> [PageLanguage]:
        return [PageLanguage("Hola", "Hola", "{algo:algo}")]
