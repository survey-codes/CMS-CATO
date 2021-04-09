from django.db import models
from django.utils.translation import ugettext_lazy as _


APP_LABEL = 'tools'

LANGUAGE = _('Language')
LANGUAGE_PLURAL = _('Languages')
LANGUAGE_NAME = _('Language Name')
LANGUAGE_ABBREVIATION = _('Language abbreviation')
MAX_LENGTH_NAME = 25
MAX_LENGTH_ABBREVIATION = 2


class Language(models.Model):
    name = models.CharField(verbose_name=LANGUAGE_NAME, max_length=MAX_LENGTH_NAME, unique=True)
    abbreviation = models.CharField(verbose_name=LANGUAGE_ABBREVIATION, max_length=MAX_LENGTH_ABBREVIATION)

    class Meta:
        verbose_name = LANGUAGE
        verbose_name_plural = LANGUAGE_PLURAL
        app_label = APP_LABEL

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'
