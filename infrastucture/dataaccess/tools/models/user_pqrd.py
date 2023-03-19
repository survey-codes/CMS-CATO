from django.db import models
from django.utils.translation import ugettext_lazy as _

from infrastucture.constants import TOOLS_APP_LABEL
from infrastucture.dataaccess.main.models.audit import Audit


class UserPqrd(Audit):
    __EMAIL = _("Email")
    email = models.EmailField(
        verbose_name=__EMAIL,
        blank=True,
        null=True
    )

    class Meta:
        __USER = _("User")
        __USERS = _("Users")

        app_label = TOOLS_APP_LABEL
        verbose_name = __USER
        verbose_name_plural = __USERS

    def __str__(self):
        return self.email

    def get_app_label(self):
        return self._meta.app_label

    def get_model_name(self):
        return self._meta.model_name
