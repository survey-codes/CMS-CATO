from graphene import ObjectType, List, String

from domain.entity.language import Language
from domain.services.language_service import LanguageService


class LanguageQuery(ObjectType):
    languages = List(Language, abbreviation=String())

    def resolve_languages(self, info, abbreviation=None, **kwargs):
        language_service = LanguageService()
        return language_service.select(abbreviation=abbreviation)
