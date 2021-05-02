from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.infrastructure.data_access.constants import MENU_NAME, MAX_LENGTH_NAME, MENUS_APP_LABEL
from cms.infrastructure.data_access.entities.main.language_abstract import LanguageAbstract
from cms.infrastructure.data_access.entities.menus.menu import Menu


class MenuLanguage(LanguageAbstract):
    """

    """
    __EMPTY_STRING = ""
    __MENU_TRANSLATIONS = 'translations'

    name = models.CharField(verbose_name=MENU_NAME, max_length=MAX_LENGTH_NAME, default=__EMPTY_STRING)
    menu = models.ForeignKey(Menu, related_name=__MENU_TRANSLATIONS, on_delete=models.CASCADE)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)

    class Meta:
        __MENU_LANGUAGE = _('Menu language')
        __MENU_LANGUAGE_PLURAL = _('Menu languages')

        verbose_name = __MENU_LANGUAGE
        verbose_name_plural = __MENU_LANGUAGE_PLURAL
        unique_together = (("language", "menu"),)
        app_label = MENUS_APP_LABEL

    def __str__(self):
        return self.menu.name
