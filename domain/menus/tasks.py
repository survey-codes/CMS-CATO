from celery.task import task
from celery.utils.log import get_logger

from domain.menus.models import Menu, MenuItem, MenuLanguage, MenuItemLanguage


logger = get_logger(__name__)


def _get_menu_items(menu, language):
    """

    """

    items = []
    menu_items = menu.items.all()
    for item in menu_items:
        item_translation = item.translations.filter(language=language).first()
        if item_translation:
            items.append(item_translation.metadata)

    return items


@task(name='menu_update_jsonfield', ignore_result=True)
def menu_update_jsonfield(menu_id):
    """
    Update the JSON field of the translations available for a menu.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """

    try:
        menu = Menu.objects.get(pk=menu_id)
        logger.debug(f'Found menu: {menu}')

        # Loop menu translations
        menu_translations = menu.translations.all()
        for translation in menu_translations:
            translation.metadata = {
                'name': translation.name,
                'items': _get_menu_items(menu, translation.language)
            }

        translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving menu: \n{e}')


@task(name='', ignore_result=True)
def menuitem_update_jsonfield(menuitem_id):
    """

    """

    try:
        menuitem = MenuItem.objects.get(pk=menuitem_id)
        logger.debug(f'Found menu: {menuitem}')

        # Loop menuitem translations
        pass

    except Exception as e:
        logger.warning(f'Error retrieving menuitem: \n{e}')
