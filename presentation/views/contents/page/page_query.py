from graphene import ObjectType, List, String

from presentation.dto.page_dto import PageDto
from presentation.presenter.contents.page.page_presenter import PagePresenter


class PageQuery(ObjectType):
    pages = List(
        PageDto,
        lang=String(description='Filtrar búsqueda por idioma'),
        slug=String(description='Buscar una página por su SLUG')
    )

    def resolve_pages(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        slug = kwargs.get('slug', '')
        page_presenter = PagePresenter()
        return page_presenter.select(lang, slug)
