from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.main.models import Audit, LanguageAbstract
from mptt.models import MPTTModel

APP_LABEL = 'menus'

MAX_LENGTH_NAME = 100
MAX_LENGTH_URL = 255

MENU = _('Menu')
MENU_CHILDREN = 'children'
MENU_GENERAL = _('Is a general menu')
MENU_GENERAL_ERROR = _('There cannot be more than one general menu')
MENU_ITEM = _('Menu item')
MENU_ITEM_LANGUAGE = _('Menu item language')
MENU_ITEM_LANGUAGE_PLURAL = _('Menu item languages')
MENU_ITEM_NAME = _('Item name')
MENU_ITEM_PARENT = _('Menu item parent')
MENU_ITEM_PLURAL = _('Menu items')
MENU_ITEM_TRANSLATIONS = _('translations')
MENU_ITEM_URL = _('URL')
MENU_ITEMS = 'items'
MENU_LANGUAGE = _('Menu language')
MENU_LANGUAGE_PLURAL = _('Menu languages')
MENU_NAME = _('Menu name')
MENU_PLURAL = _('Menus')
MENU_TRANSLATIONS = 'translations'


class Menu(Audit):
    """

    """

    name = models.CharField(verbose_name=MENU_NAME, max_length=MAX_LENGTH_NAME)
    is_general = models.BooleanField(verbose_name=MENU_GENERAL, default=False)

    class Meta:
        verbose_name = MENU
        verbose_name_plural = MENU_PLURAL
        app_label = APP_LABEL

    def clean(self):
        queryset = Menu.objects.filter(is_general=True)
        if queryset.exists():
            raise ValidationError({
                "general": MENU_GENERAL_ERROR
            })

    def __str__(self):
        return self.name


class MenuLanguage(LanguageAbstract):
    """

    """

    name = models.CharField(verbose_name=MENU_NAME, max_length=MAX_LENGTH_NAME, default='')
    menu = models.ForeignKey(Menu, related_name=MENU_TRANSLATIONS, on_delete=models.CASCADE)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)

    class Meta:
        verbose_name = MENU_LANGUAGE
        verbose_name_plural = MENU_LANGUAGE_PLURAL
        unique_together = (("language", "menu"),)
        app_label = APP_LABEL

    def __str__(self):
        return self.menu.name


class MenuItem(MPTTModel, Audit):
    """

    """

    name = models.CharField(verbose_name=MENU_ITEM_NAME, max_length=MAX_LENGTH_NAME)
    link = models.CharField(verbose_name=MENU_ITEM_URL, max_length=MAX_LENGTH_URL, blank=True)
    menu = models.ForeignKey(
        Menu,
        verbose_name=MENU,
        related_name=MENU_ITEMS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    parent = models.ForeignKey(
        "self",
        verbose_name=MENU_ITEM_PARENT,
        related_name=MENU_CHILDREN,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = MENU_ITEM
        verbose_name_plural = MENU_ITEM_PLURAL
        app_label = APP_LABEL

    def __str__(self):
        return self.name


class MenuItemLanguage(LanguageAbstract):
    """

    """

    name = models.CharField(verbose_name=MENU_ITEM_NAME, max_length=MAX_LENGTH_NAME)
    metadata = JSONField(default=dict, encoder=DjangoJSONEncoder, editable=False)
    menuitem = models.ForeignKey(MenuItem, related_name=MENU_ITEM_TRANSLATIONS, on_delete=models.CASCADE)

    class Meta:
        verbose_name = MENU_ITEM_LANGUAGE
        verbose_name_plural = MENU_ITEM_LANGUAGE_PLURAL
        unique_together = (("language", "menuitem"),)
        app_label = APP_LABEL

    def __str__(self):
        return self.name
