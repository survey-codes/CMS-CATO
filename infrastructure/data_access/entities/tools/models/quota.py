from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import TOOLS_APP_LABEL, TYPE_KEY
from infrastructure.data_access.entities.main.audit import Audit
from presentation.constants import MAIL_KEY


class Quota(Audit):
    __AMOUNT = _("Amount")
    __QUOTA_DEFAULT = 0
    __MAIL = _("Mail")
    __SMS = _("Sms")
    __SMS_KEY = "sms"
    __TYPE = _("Type")
    __TYPE_CHOICES = (
        (MAIL_KEY, __MAIL),
        (__SMS_KEY, __SMS)
    )
    __MAX_LENGTH_CHOICES = 4

    amount = models.PositiveIntegerField(
        verbose_name=__AMOUNT,
        default=__QUOTA_DEFAULT
    )
    type = models.CharField(
        verbose_name=__TYPE,
        choices=__TYPE_CHOICES,
        max_length=__MAX_LENGTH_CHOICES,
        blank=True,
        null=True
    )

    class Meta:
        app_label = TOOLS_APP_LABEL
        unique_together = (TYPE_KEY,)

    @property
    def zero_quota(self):
        return self.amount == self.__QUOTA_DEFAULT

    def subtract_quota(self, count):
        self.amount -= count

    def __str__(self):
        return f"{self.get_type_display()} ({self.amount})"
