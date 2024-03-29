from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# from infrastucture.dataaccess.utilities.menu_tasks import menuitem_update_jsonfield
from infrastucture.constants import MENU_ITEM_NAME, MAX_LENGTH_NAME, MENU, MENUS_APP_LABEL
from infrastucture.dataaccess.main.models.audit import Audit
from infrastucture.dataaccess.menus.models.menu import Menu


class MenuItem(MPTTModel, Audit):
    """

    """
    __MENU_ITEM_URL = _('URL')
    __MAX_LENGTH_URL = 255
    __MENU_ITEMS = 'items'
    __MENU_ITEM_PARENT = _('Menu item parent')
    __MENU_CHILDREN = 'children'

    name = models.CharField(
        verbose_name=MENU_ITEM_NAME,
        max_length=MAX_LENGTH_NAME
    )

    link = models.CharField(
        verbose_name=__MENU_ITEM_URL,
        max_length=__MAX_LENGTH_URL,
        blank=True
    )

    menu = models.ForeignKey(
        Menu,
        verbose_name=MENU,
        related_name=__MENU_ITEMS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    parent = TreeForeignKey(
        "self",
        verbose_name=__MENU_ITEM_PARENT,
        related_name=__MENU_CHILDREN,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        __MENU_ITEM = _('Menu item')
        __MENU_ITEM_PLURAL = _('Menu items')

        verbose_name = __MENU_ITEM
        verbose_name_plural = __MENU_ITEM_PLURAL
        app_label = MENUS_APP_LABEL

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.link = f"/{slugify(self.name)}"
        super(MenuItem, self).save(*args, **kwargs)
        # Run background tasks on translations
        # TODO: Revisar esto
        # menuitem_update_jsonfield.apply_async(kwargs={'menuitem_id': self.pk}, countdown=10)
