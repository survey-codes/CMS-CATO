import graphene

from presentation.contents.api.scalars import JSONCustom
from domain.entities.contents import models
from scalars import JSONCustom


class GeneralInfoQuery(graphene.ObjectType):
    general_info = JSONCustom(
        lang=graphene.String(description='Obtener información general en un idioma específico')
    )

    def resolve_general_info(self, info, **kwargs):
        lang = kwargs.get('lang', 'ES')
        data = {
            'header': dict(),
            'footer': None
        }

        general_info = models.GeneralData.objects.filter(slug_general_data='general-data').first()
        assert general_info, 'No existe información general'

        menu = models.Menu.objects.filter(general=True).first()
        assert general_info, 'No existe un menú general'

        info_lang = general_info.general_data_lang.filter(language__abbreviation=lang).first()
        if info_lang:
            data['footer'] = info_lang.general_metadata['footer']
            menu_lang = menu.menu_lang.filter(language__abbreviation=lang).first()

            if menu_lang:
                data['header'] = {
                    'logo': info_lang.general_metadata['logo'],
                    'menu': menu_lang.menu_metadata['menu']
                }
            else:
                menu_lang = menu.menu_lang.filter(language__abbreviation='ES').first()
                data['header'] = {
                    'logo': info_lang.general_metadata['logo'],
                    'menu': menu_lang.menu_metadata['menu']
                }
        else:
            info_lang = general_info.general_data_lang.filter(
                language__abbreviation='ES'
            ).first()
            menu_lang = menu.menu_lang.filter(language__abbreviation='ES').first()
            data['footer'] = info_lang.general_metadata['footer']
            data['header'] = {
                'logo': info_lang.general_metadata['logo'],
                'menu': menu_lang.menu_metadata['menu']
            }

        return data


class PageQuery(graphene.ObjectType):
    page = JSONCustom(
        slug=graphene.String(description='Buscar una página por su slug', required=True),
        lang=graphene.String(description='Filtrar búsqueda por idioma')
    )

    def resolve_page(self, info, **kwargs):
        slug = kwargs.get('slug', None)
        lang = kwargs.get('lang', 'ES')
        assert slug, 'Debe proporcionar al menos el slug de la página'

        page = models.Page.objects.filter(slug_page=slug).first()
        assert page, f'No se encontró la página con slug {slug}:'

        page_lang = page.page_lang.filter(language__abbreviation=lang).first()
        if page_lang:
            data = page_lang.page_metadata

        # Return the default language translation
        else:
            page_lang = page.page_lang.filter(language__abbreviation='ES').first()
            data = page_lang.page_metadata

        return data
