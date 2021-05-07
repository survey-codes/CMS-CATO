import graphene

from cms.infrastructure.data_access.entities.contents import models
from .scalars import JSONCustom


class GeneralInfoQuery(graphene.ObjectType):
    general_info = JSONCustom(
        lang=graphene.String(description='Filtrar búsqueda por idioma')
    )

    def resolve_general_info(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')

        info_translations = models.GeneralDataLanguage.objects.all()
        assert info_translations.exists(), 'No existe información general del sitio'

        if lang:
            info = info_translations.select_related('language').filter(language__abbreviation=lang)
            if info.exists():
                return info.first().metadata

        # Default language translation
        else:
            info = info_translations.filter(language__abbreviation='ES')
            assert info.exists(), f'No se encontró ninguna traducción para la información general del sitio'
            return info.first().metadata


class PageQuery(graphene.ObjectType):
    page = JSONCustom(
        slug=graphene.String(description='Buscar una página por su slug', required=True),
        lang=graphene.String(description='Filtrar búsqueda por idioma')
    )

    def resolve_page(self, info, **kwargs):
        slug = kwargs.get('slug', None)
        lang = kwargs.get('lang', None)
        assert slug, 'Debe proporcionar al menos el slug de la página'

        page_translations = models.PageLanguage.objects.filter(page__slug=slug)
        assert page_translations.exists(), f'No existe la página {slug}'

        if lang:
            data = page_translations.filter(language__abbreviation=lang)
            if data.exists():
                return data.first().metadata

            # Default language translation
            else:
                data = models.PageLanguage.objects.filter(language__abbreviation='ES')
                assert data.exists(), f'No se encontró ninguna traducción para la página {slug}'
                return data.first().metadata
