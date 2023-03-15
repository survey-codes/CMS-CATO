from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from infrastucture.constants import MENU_ITEM_NAME, MAX_LENGTH_NAME, MENUS_APP_LABEL
from infrastucture.main.models.language_abstract import LanguageAbstract
from infrastucture.menus.models.menu_item import MenuItem


class MenuItemLanguage(LanguageAbstract):
    """

    """
    __MENU_ITEM_TRANSLATIONS = _('translations')

    name = models.CharField(verbose_name=MENU_ITEM_NAME, max_length=MAX_LENGTH_NAME)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)
    menuitem = models.ForeignKey(MenuItem, related_name=__MENU_ITEM_TRANSLATIONS, on_delete=models.CASCADE)

    class Meta:
        __MENU_ITEM_LANGUAGE = _('Menu item language')
        __MENU_ITEM_LANGUAGE_PLURAL = _('Menu item languages')

        verbose_name = __MENU_ITEM_LANGUAGE
        verbose_name_plural = __MENU_ITEM_LANGUAGE_PLURAL
        unique_together = (("language", "menuitem"),)
        app_label = MENUS_APP_LABEL

    def __str__(self):
        return self.name
