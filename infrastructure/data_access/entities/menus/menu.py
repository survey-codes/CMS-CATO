from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.utilities.menu_tasks import menu_update_jsonfield
from infrastructure.data_access.constants import MENU, MENUS_APP_LABEL, MENU_NAME, MAX_LENGTH_NAME
from infrastructure.data_access.entities.main.audit import Audit


class Menu(Audit):
    """

    """
    __MENU_GENERAL = _('Is a general menu')
    __MENU_GENERAL_ERROR = _('There cannot be more than one general menu')

    name = models.CharField(verbose_name=MENU_NAME, max_length=MAX_LENGTH_NAME)
    is_general = models.BooleanField(verbose_name=__MENU_GENERAL, default=False)

    class Meta:
        __MENU_PLURAL = _('Menus')
        verbose_name = MENU
        verbose_name_plural = __MENU_PLURAL
        app_label = MENUS_APP_LABEL

    def clean(self):
        queryset = Menu.objects.filter(is_general=True)
        if queryset.exists():
            raise ValidationError({
                "general": self.__MENU_GENERAL_ERROR
            })

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)
        # Run background tasks on translations
        menu_update_jsonfield.apply_async(kwargs={'menu_id': self.pk}, countdown=10)
