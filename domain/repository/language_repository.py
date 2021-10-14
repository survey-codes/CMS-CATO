from domain.entity.language import Language


class LanguageRepository:
    def select(self) -> [Language]:
        pass

    def select_by_abbreviation(self, abbreviation: str) -> Language:
        pass
