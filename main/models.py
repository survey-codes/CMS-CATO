from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from projectCato.settings import constants as c
from tools.models import Language


class Audit(models.Model):
    creation_date = models.DateTimeField(
        verbose_name=c.CREATION_DATE,
        auto_now_add=True,
        null=True,
    )

    created_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name=c.CREATED_BY,
        on_delete=models.CASCADE,
        related_name=c.RELATED_NAME.format('created_by')
    )

    update_date = models.DateTimeField(
        verbose_name=c.UPDATED,
        default=timezone.now
    )

    updated_by = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name=c.UPDATED_BY,
        on_delete=models.CASCADE,
        related_name=c.RELATED_NAME.format('updated_by'),
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
        return c.LANGUAGE_MESSAGE
