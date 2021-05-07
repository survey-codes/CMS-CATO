from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.infrastructure.data_access.constants import TOOLS_APP_LABEL
from cms.infrastructure.data_access.entities.main.audit import Audit
from cms.presentation.constants import MAIL_KEY, DEFAULT_NUMBER, MAIL


class Quota(Audit):
    __AMOUNT = _("Amount")
    __SMS = _("Sms")
    __SMS_KEY = "sms"
    __TYPE = _("Type")
    __TYPE_CHOICES = (
        (MAIL_KEY, MAIL),
        (__SMS_KEY, __SMS)
    )
    __MAX_LENGTH_CHOICES = 4

    amount = models.PositiveIntegerField(
        verbose_name=__AMOUNT,
        default=DEFAULT_NUMBER
    )
    type = models.CharField(
        verbose_name=__TYPE,
        choices=__TYPE_CHOICES,
        max_length=__MAX_LENGTH_CHOICES,
        blank=True,
        null=True
    )

    class Meta:
        __TYPE_KEY = "type"
        app_label = TOOLS_APP_LABEL
        unique_together = (__TYPE_KEY,)

    @property
    def zero_quota(self):
        return self.amount == DEFAULT_NUMBER

    def subtract_quota(self, count):
        self.amount -= count

    def __str__(self):
        return f"{self.get_type_display()} ({self.amount})"
