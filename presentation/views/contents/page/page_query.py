from graphene import ObjectType, List, String

from domain.entity.page_language import PageLanguage
from domain.repository.page_language_repository import PageLanguageRepository
from domain.services.page_languege_service import PageLanguageService
from infrastucture.dataaccess.contents.repository.page_language_repository_impl import PageLanguageRepositoryImpl
from presentation.presenter.contents.page.page_presenter import PagePresenter


class PageQuery(ObjectType):
    pages = List(
        PageLanguage,
        lang=String(description='Filtrar búsqueda por idioma'),
        slug=String(description='Buscar una página por su SLUG', required=True)
    )

    def resolve_pages(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        slug = kwargs.get('slug', '')
        page_presenter = PagePresenter()
        return page_presenter.select(lang, slug)
