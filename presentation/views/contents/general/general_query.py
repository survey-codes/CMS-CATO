from graphene import ObjectType, String

from infrastucture.dataaccess.contents.api.scalars import JSONCustom


class GeneralQuery(ObjectType):
    general = JSONCustom(lang=String(description='Filtrar búsqueda por idioma'))

    def resolve_general(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
