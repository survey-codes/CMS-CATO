from django.db import models

from projectCato.settings import constants as c


class Language(models.Model):
    name = models.CharField(
        c.LANGUAGE_NAME,
        max_length=25,
        unique=True
    )

    abbreviation = models.CharField(
        c.LANGUAGE_ABB,
        max_length=2
    )

    class Meta:
        verbose_name = c.LANGUAGE_TAB
        verbose_name_plural = c.LANGUAGE_APP_PLURAL

    def save(self, *args, **kwargs):
        self.abbreviation = self.abbreviation.upper()
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return '{} ({})'.format(self.name, self.abbreviation)
