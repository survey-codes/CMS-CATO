from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from presentation.tools.models import Language
from projectCato.settings import constants as c

CREATION_DATE = _('creation date')
CREATED_BY = _('Created by')
UPDATED_DATE = _('Updated')
UPDATED_BY = _('Updated by')
RELATED_NAME = '%(class)s_{}'
LANGUAGE_MESSAGE = _('the same language shouldn\'t be chosen more than once')


class Audit(models.Model):
    creation_date = models.DateTimeField(
        verbose_name=CREATION_DATE,
        auto_now_add=True,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        verbose_name=CREATED_BY,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name=RELATED_NAME.format('created_by')
    )

    update_date = models.DateTimeField(
        verbose_name=UPDATED_DATE,
        auto_now=True
    )

    updated_by = models.ForeignKey(
        User,
        verbose_name=UPDATED_BY,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name=RELATED_NAME.format('updated_by'),
    )

    active = models.BooleanField(
        verbose_name=c.ACTIVE,
        default=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.id:
            self.created_by = user
        else:
            self.updated_by = user
        super(Audit, self).save(*args, **kwargs)


class LanguageAbstract(models.Model):
    language = models.ForeignKey(
        Language,
        verbose_name=c.LANGUAGE_TAB,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.language)

    def unique_error_message(self):
        return LANGUAGE_MESSAGE
