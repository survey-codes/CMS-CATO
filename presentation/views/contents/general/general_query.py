from graphene import ObjectType, String, Field

from presentation.dto.general_dto import GeneralDto
from presentation.presenter.contents.general.general_presenter import GeneralPresenter


class GeneralQuery(ObjectType):
    generals = Field(GeneralDto, lang=String(description='Filtrar búsqueda por idioma'))

    def resolve_generals(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        general_presenter: GeneralPresenter = GeneralPresenter()
        return general_presenter.select(lang)
