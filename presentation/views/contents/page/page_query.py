from graphene import ObjectType, List, String

from domain.entity.page_language import PageLanguage
from domain.repository.page_language_repository import PageLanguageRepository
from domain.services.page_languege_service import PageLanguageService
from infrastucture.dataaccess.contents.repository.page_language_repository_impl import PageLanguageRepositoryImpl


class PageQuery(ObjectType):
    pages = List(
        PageLanguage,
        lang=String(description='Filtrar búsqueda por idioma'),
        slug=String(description='Buscar una página por su SLUG', required=True)
    )

    def resolve_pages(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        page_language_repository: PageLanguageRepository = PageLanguageRepositoryImpl()
        page_language_service = PageLanguageService(page_language_repository)
        return page_language_service.select(lang)
