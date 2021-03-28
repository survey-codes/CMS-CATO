from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

from main.models import Audit, LanguageAbstract
from mptt.models import MPTTModel
from projectCato.settings import constants as c


class Menu(Audit):
    name = models.CharField(
        verbose_name=c.MENU_NAME,
        max_length=128
    )

    general = models.BooleanField(
        verbose_name=c.MENU_GENERAL,
        default=False,
    )

    class Meta:
        ordering = ("pk",)

    def clean(self):
        qs = Menu.objects.filter(general=True).first()
        if self.general and qs != self:
            raise ValidationError({
                "general": c.MENU_GENERAL_ERROR
            })

    def __str__(self):
        return self.name


class MenuLanguage(LanguageAbstract):
    menu = models.ForeignKey(
        Menu,
        related_name="menu_lang",
        on_delete=models.CASCADE
    )

    menu_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        verbose_name = c.MENU_LANGUAGE
        unique_together = (("language", "menu"),)

    def __str__(self):
        return self.menu.name


class MenuItem(MPTTModel, Audit):
    name = models.CharField(
        verbose_name=c.MENU_ITEM_NAME,
        max_length=128
    )

    menu = models.ForeignKey(
        Menu,
        verbose_name=c.MENU,
        related_name="items",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    parent = models.ForeignKey(
        "self",
        verbose_name=c.MENU_ITEM_PARENT,
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE
    )

    # Usarlos dependiendo del tipo de enlace que necesite guardar
    url = models.URLField(
        verbose_name=c.EXTERNAL_URL,
        max_length=256,
        blank=True,
        null=True
    )

    page_url = models.CharField(
        verbose_name=c.PAGE_URL,
        max_length=128,
        blank=True,
        null=True
    )

    slug_url = models.CharField(
        verbose_name="URL "+c.SLUG,
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        # ordering = ("pk",)
        verbose_name = c.MENU_ITEM

    def clean(self):
        if self.page_url and self.url:
            raise ValidationError(
                {
                    "url": c.MENU_ITEM_URL_ERROR,
                }
            )

    def get_ordering_queryset(self):
        return self.menu.items.all() if not self.parent else self.parent.children.all()

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
        verbose_name=c.MENU_NAME,
        max_length=128
    )

    menu_item = models.ForeignKey(
        MenuItem,
        related_name="item_lang",
        on_delete=models.CASCADE
    )

    menu_item_metadata = JSONField(
        verbose_name=c.JSON_CONTENT,
        blank=True,
        null=True,
        default=dict,
        encoder=DjangoJSONEncoder,
        editable=False
    )

    class Meta:
        verbose_name = c.MENU_ITEM_LANGUAGE
        unique_together = (("language", "menu_item"),)

    def __str__(self):
        return self.name
