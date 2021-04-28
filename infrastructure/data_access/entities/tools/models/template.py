from django.db import models
from django.utils.translation import ugettext_lazy as _

from infrastructure.data_access.constants import NAME, MAX_LENGTH_200, TEMPLATE, TOOLS_APP_LABEL
from infrastructure.data_access.entities.main.audit import Audit


class Template(Audit):
    __TEMPLATE_ID = _("Template ID")

    name = models.CharField(
        verbose_name=NAME,
        max_length=MAX_LENGTH_200
    )
    template_id = models.CharField(
        verbose_name=__TEMPLATE_ID,
        max_length=MAX_LENGTH_200
    )

    class Meta:
        __TEMPLATES = _("Templates")

        verbose_name = TEMPLATE
        verbose_name_plural = __TEMPLATES
        app_label = TOOLS_APP_LABEL

    def __str__(self):
        return self.name
