from graphene import ObjectType, String, List

from domain.main.contents.entity.general_language import GeneralDataLanguage
from domain.main.contents.repository.general_language_repository import GeneralDataLanguageRepository
from domain.main.contents.services.general_service import GeneralService
from infrastucture.contents.repository.general_data_language_repository_imp import GeneralDataLanguageRepositoryImpl


class GeneralQuery(ObjectType):
    generals = List(GeneralDataLanguage, lang=String(description='Filtrar búsqueda por idioma'))

    def resolve_generals(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        general_language_repository: GeneralDataLanguageRepository = GeneralDataLanguageRepositoryImpl()
        general_service = GeneralService(general_language_repository)
        return general_service.select(lang)
