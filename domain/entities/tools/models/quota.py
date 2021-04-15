from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import TOOLS_APP_LABEL, TYPE_KEY
from domain.entities.main.models import Audit
from presentation.constants import MAIL_KEY

QUOTA_DEFAULT = 0
MAIL = _("Mail")
SMS = _("Sms")
SMS_KEY = "sms"
AMOUNT = _("Amount")
AMOUNT_KEY = "amount"
TYPE = _("Type")
TYPE_CHOICES = (
    (MAIL_KEY, MAIL),
    (SMS_KEY, SMS)
)
MAX_LENGTH_CHOICES = 4


class Quota(Audit):
    amount = models.PositiveIntegerField(
        verbose_name=AMOUNT,
        default=QUOTA_DEFAULT
    )
    type = models.CharField(
        verbose_name=TYPE,
        choices=TYPE_CHOICES,
        max_length=MAX_LENGTH_CHOICES,
        blank=True,
        null=True
    )

    class Meta:
        app_label = TOOLS_APP_LABEL
        unique_together = (TYPE_KEY,)

    @property
    def zero_quota(self):
        return self.amount == QUOTA_DEFAULT

    def subtract_quota(self, count):
        self.amount -= count

    def __str__(self):
        return f"{self.get_type_display()} ({self.amount})"
