from django.db import models
from django.utils.translation import ugettext_lazy as _

from infrastructure.data_access.constants import TOOLS_APP_LABEL
from infrastructure.data_access.entities.main.audit import Audit


class Language(Audit):
    __LANGUAGE_NAME = _('Language Name')
    __LANGUAGE_ABBREVIATION = _('Language abbreviation')
    __MAX_LENGTH_NAME = 25
    __MAX_LENGTH_ABBREVIATION = 2

    name = models.CharField(verbose_name=__LANGUAGE_NAME, max_length=__MAX_LENGTH_NAME, unique=True)
    abbreviation = models.CharField(verbose_name=__LANGUAGE_ABBREVIATION, max_length=__MAX_LENGTH_ABBREVIATION)

    class Meta:
        __LANGUAGE = _('Language')
        __LANGUAGE_PLURAL = _('Languages')

        verbose_name = __LANGUAGE
        verbose_name_plural = __LANGUAGE_PLURAL
        app_label = TOOLS_APP_LABEL

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'
