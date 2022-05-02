from graphene import ObjectType, List, String

from domain.main.tools.entity.language import Language
from domain.main.tools.repository.language_repository import LanguageRepository
from domain.main.tools.services.language_service import LanguageService
from infrastucture.tools.repository.language_repository_impl import LanguageRepositoryImpl


class LanguageQuery(ObjectType):
    languages = List(Language, abbreviation=String())

    def resolve_languages(self, info, abbreviation=None, **kwargs):
        language_repository: LanguageRepository = LanguageRepositoryImpl()
        language_service = LanguageService(language_repository)
        return language_service.select(abbreviation=abbreviation)
