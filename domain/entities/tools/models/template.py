from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import NAME, MAX_LENGTH_200, TEMPLATE, TOOLS_APP_LABEL
from domain.entities.main.models import Audit

TEMPLATE_ID = _("Template ID")
TEMPLATES = _("Templates")


class Template(Audit):
    name = models.CharField(
        verbose_name=NAME,
        max_length=MAX_LENGTH_200
    )
    template_id = models.CharField(
        verbose_name=TEMPLATE_ID,
        max_length=MAX_LENGTH_200
    )

    class Meta:
        verbose_name = TEMPLATE
        verbose_name_plural = TEMPLATES
        app_label = TOOLS_APP_LABEL

    def __str__(self):
        return self.name
