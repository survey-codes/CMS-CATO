from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import LANGUAGE_APP_PLURAL, LANGUAGE_TAB

APP_LABEL = "tools"

LANGUAGE_NAME = _('Language Name')
LANGUAGE_ABB = _('Language abbreviation')
MAX_LENGTH_NAME = 25
MAX_LENGTH_ABBREVIATION = 2


class Language(models.Model):
    name = models.CharField(
        verbose_name=LANGUAGE_NAME,
        max_length=MAX_LENGTH_NAME,
        unique=True
    )

    abbreviation = models.CharField(
        verbose_name=LANGUAGE_ABB,
        max_length=MAX_LENGTH_ABBREVIATION
    )

    class Meta:
        verbose_name = LANGUAGE_TAB
        verbose_name_plural = LANGUAGE_APP_PLURAL
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'
