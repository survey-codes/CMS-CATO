from graphene import ObjectType, String, List

from domain.entity.general_language import GeneralLanguage
from domain.repository.general_language_repository import GeneralLanguageRepository
from domain.services.general_service import GeneralService
from infrastucture.dataaccess.contents.repository.general_language_repository_imp import GeneralLanguageRepositoryImpl


class GeneralQuery(ObjectType):
    generals = List(GeneralLanguage, lang=String(description='Filtrar búsqueda por idioma'))

    def resolve_generals(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        general_language_repository: GeneralLanguageRepository = GeneralLanguageRepositoryImpl()
        general_service = GeneralService(general_language_repository)
        return general_service.select(lang)
