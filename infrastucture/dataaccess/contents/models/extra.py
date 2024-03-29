from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from infrastucture.dataaccess.contents.constants import PATH_APP, APP_LABEL
from infrastucture.dataaccess.main.models.audit import Audit
from infrastucture.dataaccess.main.models.language_abstract import LanguageAbstract
from infrastucture.dataaccess.menus.models.menu import Menu
# from infrastucture.dataaccess.utilities.content_tasks import info_update_jsonfield

PATH_SITE = 'site/'
PATH_SITE_LOGO = f'{PATH_APP}{PATH_SITE}logo'
ORDER = _('order')
FOOTER = _('Footer')
MAIN_MENU = _('Main menu')
SITE_LOGO = _('Site logo')
GENERAL_DATA = _('General data')
GENERAL_DATA_TRANSLATIONS = 'translations'
GENERAL_DATA_LANGUAGE = _('General data language')
GENERAL_DATA_LANGUAGE_PLURAL = _('General data languages')


class GeneralData(Audit):
    """

    """

    logo = models.ImageField(verbose_name=SITE_LOGO, upload_to=PATH_SITE_LOGO, blank=True)
    menu = models.ForeignKey(Menu, verbose_name=MAIN_MENU, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-active', 'creation_date']
        verbose_name = GENERAL_DATA
        verbose_name_plural = GENERAL_DATA
        app_label = APP_LABEL

    def __str__(self):
        return 'Site info'

    def save(self, *args, **kwargs):
        super(GeneralData, self).save(*args, **kwargs)
        # Run background tasks on translations
        # TODO: Revisar que paso con estas task
        # info_update_jsonfield.apply_async(kwargs={'info_id': self.pk}, countdown=5)


class GeneralDataLanguage(LanguageAbstract):
    """

    """

    footer = RichTextField(verbose_name=FOOTER, blank=True)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)
    info = models.ForeignKey(GeneralData, related_name=GENERAL_DATA_TRANSLATIONS, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('language', 'info'),)
        verbose_name = GENERAL_DATA_LANGUAGE
        verbose_name_plural = GENERAL_DATA_LANGUAGE_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return f'{self.info}-{self.language}'
