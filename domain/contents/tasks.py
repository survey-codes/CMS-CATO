from celery import current_app
from celery.task import task
from celery.utils.log import get_logger




logger = get_logger(__name__)


@task(name='page_update_jsonfield', ignore_result=True)
def page_update_jsonfield(page_id):
    """
    Update the JSON field of the translations available for a page.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """
    from domain.contents import models
    try:
        page = models.Page.objects.get(pk=page_id)
        logger.debug(f'Found page: {page}')

        # Loop page translations
        page_translations = page.translations.all()
        for translation in page_translations:
            translation.metadata = {
                'title': translation.title,
                'description': translation.description,
                'sections': list()
            }
            if page.inner_menu:
                inner_menu = page.inner_menu.translations.filter(language=translation.language).first()
                translation.metadata['menu'] = inner_menu.metadata

            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving page: \n{e}')


@task(name='info_update_jsonfield', ignore_result=True)
def info_update_jsonfield(info_id):
    """
    Update the JSON field of the translations available for the general info.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """

    from domain.contents import models
    try:
        info = models.GeneralData.objects.get(pk=info_id)
        logger.debug(f'Found info: {info}')

        # Loop info translations
        info_translations = info.translations.all()
        for translation in info_translations:
            translation.metadata = {
                'logo': info.logo.url,
                'footer': translation.footer
            }
            if info.main_menu:
                main_menu = info.main_menu.translations.filter(language=translation.language).first()
                translation.metadata['menu'] = main_menu.metadata

            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving info: \n{e}')
