from graphene import ObjectType, String, List

from domain.entity.general_language import GeneralLanguage
from domain.services.general_service import GeneralService


class GeneralQuery(ObjectType):
    generals = List(GeneralLanguage, lang=String(description='Filtrar búsqueda por idioma'))

    def resolve_generals(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        general_service = GeneralService()
        return general_service.select(lang)
