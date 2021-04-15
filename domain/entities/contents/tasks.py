# from celery import current_app
from celery.task import task
from celery.utils.log import get_logger

logger = get_logger(__name__)


def _get_posts():
    """

    """
    pass


def _get_galleries(post_id):
    """

    """

    galleries = []
    types = ('non_gallery', 'gallery')
    from domain.entities.contents.models.posts import PostGallery
    post_galleries = PostGallery.objects.filter(post_id=post_id, active=True).order_by('order')
    type = types[post_galleries.count() > 1]
    for gallery in post_galleries:
        gallery_content = {
            'title': gallery.title,
            'image': gallery.image.url if gallery.image else None,
            'is_360': gallery.is_360,
            'youtube_url': gallery.youtube_url if gallery.youtube_url else None,
        }
        gallery_content['type'] = 'img' if gallery_content['image'] else 'youtube'
        galleries.append(gallery_content)
        if gallery_content['is_360']:
            gallery_content['type'] = 'img360'

    return galleries, type


def _get_sections(page, language):
    """

    """

    sections = []
    return sections


@task(name='page_update_jsonfield', ignore_result=True)
def page_update_jsonfield(page_id):
    """
    Update the JSON field of the translations available for a page.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """

    from domain.entities.contents.models.pages import PageLanguage
    from domain.entities.menus.models import MenuLanguage
    try:
        page_translations = PageLanguage.objects.select_related(
            'language', 'page__menu'
        ).filter(page_id=page_id)
        logger.debug(f'Retrieved {page_translations.count()} translations')

        # Loop page translations
        for translation in page_translations:
            translation.metadata = {
                'title': translation.title,
                'description': translation.description,
                'sections': list()
            }
            if translation.page.menu:
                queryset = MenuLanguage.objects.filter(menu=translation.page.menu, language=translation.language)
                if queryset.exists():
                    menu = queryset.first()
                    translation.metadata['menu'] = menu.metadata

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

    from domain.entities.contents.models import GeneralDataLanguage
    from domain.entities.menus.models import MenuLanguage
    try:
        info_translations = GeneralDataLanguage.objects.select_related(
            'language', 'info__menu'
        ).filter(info_id=info_id)
        logger.debug(f'Retrieved {info_translations.count()} translations')

        # Loop info translations
        for translation in info_translations:
            translation.metadata = {
                'logo': translation.info.logo.url,
                'footer': translation.footer
            }
            if translation.info.menu:
                queryset = MenuLanguage.objects.filter(menu=translation.info.menu, language=translation.language)
                if queryset.exists():
                    menu = queryset.first()
                    translation.metadata['menu'] = menu.metadata

            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving info: \n{e}')


@task(name='section_update_jsonfield', ignore_result=True)
def section_update_jsonfield(section_id, task_callback=None):
    """
    Update the JSON field of the translations available for a section.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """

    from domain.entities.contents.models.sections import SectionLanguage
    try:
        section_translations = SectionLanguage.objects.select_related(
            'language', 'section__template'
        ).filter(section_id=section_id)
        logger.debug(f'Retrieved {section_translations.count()} translations')

        # loop section translations
        for translation in section_translations:
            translation.metadata = {
                'title': translation.title,
                'description': translation.description,
                'background_image': translation.section.background.url,
                'background_color': translation.section.background_color,
                'template': translation.section.template.name,
                'posts': list(),
            }

            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving section: \n{e}')

    # send_task callback
    # if task_callback
    #     args, kwargs = task_callback
    #     current_app.send_task(*args, **str_keys(kwargs))


@task(name='', ignore_result=True)
def post_update_jsonfield(post_id, task_callback=None):
    """
    Update the JSON field of the translations available for a post.
    This task is triggered 10 seconds after saving a page in order to
    avoid stale data problems or non-existent references
    """

    from domain.entities.contents.models.posts import PostLanguage
    try:
        post_translations = PostLanguage.objects.select_related(
            'language', 'post__parent'
        ).filter(post_id=post_id)
        logger.debug(f'Retrieved {post_translations.count()} translations')

        # Loop translations
        for translation in post_translations:
            translation.metadata = {
                'title': translation.title,
                'description': translation.description,
                'logo': translation.post.logo.url,
                'link': translation.post.link,
                'children': list()
            }
            translation.metadata['galleries'], translation.metadata['type'] = _get_galleries(post_id)
            translation.save(update_fields=['metadata'])

    except Exception as e:
        logger.warning(f'Error retrieving post: \n{e}')

    # send_task callback
    # if task_callback
    #     args, kwargs = task_callback
    #     current_app.send_task(*args, **str_keys(kwargs))
