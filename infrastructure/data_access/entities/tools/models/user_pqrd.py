from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import TOOLS_APP_LABEL
from infrastructure.data_access.entities.main.audit import Audit

EMAIL = _("Email")
USER = _("User")
USERS = _("Users")


class UserPqrd(Audit):
    email = models.EmailField(
        verbose_name=EMAIL,
        blank=True,
        null=True
    )

    class Meta:
        app_label = TOOLS_APP_LABEL
        verbose_name = USER
        verbose_name_plural = USERS

    def __str__(self):
        return self.email
