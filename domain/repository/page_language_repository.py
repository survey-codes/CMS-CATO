from domain.entity.page_language import PageLanguage


class PageLanguageRepository:
    def select(self, lang: str, slug: str) -> [PageLanguage]:
        pass
