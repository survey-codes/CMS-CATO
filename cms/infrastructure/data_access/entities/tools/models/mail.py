from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.infrastructure.data_access.constants import TOOLS_APP_LABEL, MAX_LENGTH_200, NAME, TEMPLATE
from cms.infrastructure.data_access.entities.main.audit import Audit
from cms.infrastructure.data_access.entities.tools.models.template import Template
from cms.presentation.constants import DEFAULT_NUMBER


class Mail(Audit):
    __AMOUNT_SEND = _("Amount send")

    name = models.CharField(
        verbose_name=NAME,
        max_length=MAX_LENGTH_200
    )
    amount_send = models.PositiveIntegerField(
        verbose_name=__AMOUNT_SEND,
        default=DEFAULT_NUMBER
    )
    template = models.ForeignKey(
        Template,
        verbose_name=TEMPLATE,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        __MAIL = _("Mail")
        __MAILS = _("Mails")

        verbose_name = __MAIL
        verbose_name_plural = __MAILS
        app_label = TOOLS_APP_LABEL

    def add_to_amount_send(self, count):
        self.amount_send += count

    def __str__(self):
        return f"{self.name} ({self.amount_send})"