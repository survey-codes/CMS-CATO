from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel

from domain.constants import MAX_LENGTH_50, MENU, RELATED_NAME, JSON_CONTENT, SLUG
from domain.entities.main.models import Audit, LanguageAbstract

APP_LABEL = "menus"

MAX_LENGTH_NAME = 128
MAX_LENGTH_URL = 256
MENUS = _("Menus")
MENU_ITEM = _("Menu's item")
MENU_NAME = _("Menu's name")
MENU_GENERAL = _("General menu")
MENU_GENERAL_ERROR = _("There cannot be more than one general menu")
MENU_LANG_KEY = "menu_lang"
MENU_LANGUAGE = _("Menu language")
MENUS_LANGUAGE = _("Menu's language")
MENU_ITEM_NAME = _("Menu's item name")
ITEMS_KEY = "items"
MENU_ITEM_PARENT = _("Menu's item parent")
CHILDREN_KEY = "children"
EXTERNAL_URL = _("External url")
PAGE_URL = _("Page url")
URL = "URL"
MENU_ITEM_URL_ERROR = _("No puede añadir ambas URL, escoja solo una")
ITEM_LANG_KEY = "item_lang"
MENU_ITEM_LANGUAGE = _("Menu's item language")


class Menu(Audit):
    name = models.CharField(
        verbose_name=MENU_NAME,
        max_length=MAX_LENGTH_NAME
    )

    general = models.BooleanField(
        verbose_name=MENU_GENERAL,
        default=False,
    )

    class Meta:
        verbose_name = MENU
        verbose_name_plural = MENUS
        ordering = ("pk",)
        app_label = APP_LABEL

    def clean(self):
        qs = Menu.objects.filter(general=True).first()
        if self.general and qs != self:
            raise ValidationError({
                "general": MENU_GENERAL_ERROR
            })

    def __str__(self):
        return self.name


class MenuLanguage(LanguageAbstract):
    menu = models.ForeignKey(
        Menu,
        related_name=RELATED_NAME.format(MENU_LANG_KEY),
        on_delete=models.CASCADE
    )

    menu_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        verbose_name = MENU_LANGUAGE
        verbose_name_plural = MENUS_LANGUAGE
        unique_together = (("language", "menu"),)
        app_label = APP_LABEL

    def __str__(self):
        return self.menu.name


class MenuItem(MPTTModel, Audit):
    name = models.CharField(
        verbose_name=MENU_ITEM_NAME,
        max_length=MAX_LENGTH_NAME
    )

    menu = models.ForeignKey(
        Menu,
        verbose_name=MENU,
        related_name=RELATED_NAME.format(ITEMS_KEY),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    parent = models.ForeignKey(
        "self",
        verbose_name=MENU_ITEM_PARENT,
        null=True,
        blank=True,
        related_name=RELATED_NAME.format(CHILDREN_KEY),
        on_delete=models.CASCADE
    )

    # Usarlos dependiendo del tipo de enlace que necesite guardar
    url = models.URLField(
        verbose_name=EXTERNAL_URL,
        max_length=MAX_LENGTH_URL,
        blank=True,
        null=True
    )

    page_url = models.CharField(
        verbose_name=PAGE_URL,
        max_length=MAX_LENGTH_NAME,
        blank=True,
        null=True
    )

    slug_url = models.CharField(
        verbose_name=f"{URL} {SLUG}",
        max_length=MAX_LENGTH_50,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = MENU_ITEM
        app_label = APP_LABEL

    def clean(self):
        if self.page_url and self.url:
            raise ValidationError(
                {
                    "url": MENU_ITEM_URL_ERROR,
                }
            )

    def get_ordering_queryset(self):
        return self.menu.menuitem_items_set.all() if not self.parent else self.parent.menuitem_children_set.all()

    @property
    def linked_object(self):
        return self.page

    def get_url(self):
        linked_object = self.linked_object
        # Deprecated. To remove in #5022
        return linked_object.get_absolute_url() if linked_object else self.url

    def is_public(self):
        return not self.linked_object or getattr(
            self.linked_object, "is_published", True
        )

    def __str__(self):
        return self.name


class MenuItemLanguage(LanguageAbstract):
    name = models.CharField(
        verbose_name=MENU_NAME,
        max_length=MAX_LENGTH_NAME
    )

    menu_item = models.ForeignKey(
        MenuItem,
        related_name=RELATED_NAME.format(ITEM_LANG_KEY),
        on_delete=models.CASCADE
    )

    menu_item_metadata = JSONField(
        verbose_name=JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        verbose_name = MENU_ITEM_LANGUAGE
        unique_together = (("language", "menu_item"),)
        app_label = APP_LABEL

    def __str__(self):
        return self.name
