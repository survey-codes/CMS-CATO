from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import TOOLS_APP_LABEL, MAX_LENGTH_200, NAME, TEMPLATE
from infrastructure.data_access.entities.main.models import Audit
from infrastructure.data_access.entities.tools.models.template import Template

AMOUNT_SEND = _("Amount send")
MAIL = _("Mail")
MAILS = _("Mails")


class Mail(Audit):
    name = models.CharField(
        verbose_name=NAME,
        max_length=MAX_LENGTH_200
    )
    amount_send = models.PositiveIntegerField(
        verbose_name=AMOUNT_SEND,
        default=0
    )
    template = models.ForeignKey(
        Template,
        verbose_name=TEMPLATE,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = MAIL
        verbose_name_plural = MAILS
        app_label = TOOLS_APP_LABEL

    def add_to_amount_send(self, count):
        self.amount_send += count

    def __str__(self):
        return f"{self.name} ({self.amount_send})"
