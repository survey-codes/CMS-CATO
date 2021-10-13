from infrastucture.constants import DEFAULT_BOOL
from infrastucture.dataaccess.tools.models import Language


class LanguageService:
    language = Language.objects

    def select(self):
        return self.language.filter(active=DEFAULT_BOOL)

    def count(self):
        return self.select().count()
