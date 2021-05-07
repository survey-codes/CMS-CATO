from cms.infrastructure.data_access.entities.tools.models import Language
from cms.presentation.constants import DEFAULT_BOOL


class LanguageService:
    language = Language.objects

    def select(self):
        return self.language.filter(active=DEFAULT_BOOL)

    def count(self):
        return self.select().count()
