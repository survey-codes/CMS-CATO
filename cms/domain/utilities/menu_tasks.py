from celery.task import task
from celery.utils.log import get_logger

logger = get_logger(__name__)


def _get_children(menuitem, language):
    """

    """
    pass


def _get_menu_items(menu, language):
    """

    """

    from cms.infrastructure.data_access.entities.menus.menu_item_language import MenuItemLanguage
    items = []
    item_translations = MenuItemLanguage.objects.filter(menuitem__menu=menu, language=language)
    for item in item_translations:
        items.append(item.metadata)

    return items


@task(name='menu_update_jsonfield', ignore_result=True)
def menu_update_jsonfield(menu_id):
    """
    Update the JSON field of the translations available for a menu.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """

    from cms.infrastructure.data_access.entities.menus.menu_language import MenuLanguage
    try:
        menu_translations = MenuLanguage.objects.select_related(
            'language', 'menu'
        ).filter(menu_id=menu_id)
        logger.debug(f'Retrieved {menu_translations.count()} translations')

        # Loop menu translations
        for translation in menu_translations:
            translation.metadata = {
                'name': translation.name,
                'items': _get_menu_items(translation.menu, translation.language)
            }

            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving menu: \n{e}')


@task(name='menuitem_update_jsonfield', ignore_result=True)
def menuitem_update_jsonfield(menuitem_id):
    """

    """

    from cms.infrastructure.data_access.entities.menus.menu_item_language import MenuItemLanguage
    try:
        item_translations = MenuItemLanguage.objects.select_related(
            'language', 'menuitem__parent'
        ).filter(menuitem_id=menuitem_id)
        logger.debug(f'Retrieved {item_translations.count()} translations')

        # Loop menuitem translations
        for translation in item_translations:
            translation.metadata = {
                'name': translation.name,
                'url': translation.menuitem.link,
                'children': list()
            }

            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving menuitem: \n{e}')
