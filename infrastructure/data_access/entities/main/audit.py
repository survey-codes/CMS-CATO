from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from domain.constants import RELATED_NAME


class Audit(models.Model):
    """

    """
    __ACTIVE = _('Active')
    __CREATION_DATE = _('Creation date')
    __CREATION_DATE_KEY = 'creation_date'
    __CREATED_BY = _('Created by')
    __CREATED_BY_KEY = 'created_by'
    __UPDATED_DATE = _('Updated')
    __UPDATE_DATE_KEY = 'update_date'
    __UPDATED_BY = _('Updated by')
    __UPDATED_BY_KEY = 'updated_by'

    creation_date = models.DateTimeField(
        verbose_name=__CREATION_DATE,
        auto_now_add=True,
        null=True,
    )

    created_by = models.ForeignKey(
        User,
        verbose_name=__CREATED_BY,
        on_delete=models.CASCADE,
        null=True,
        related_name=RELATED_NAME.format(__CREATED_BY_KEY)
    )

    update_date = models.DateTimeField(
        verbose_name=__UPDATED_DATE,
        auto_now=True
    )

    updated_by = models.ForeignKey(
        User,
        verbose_name=__UPDATED_BY,
        on_delete=models.CASCADE,
        null=True,
        related_name=RELATED_NAME.format(__UPDATED_BY_KEY),
    )

    active = models.BooleanField(verbose_name=__ACTIVE, default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.created_by = user
        else:
            self.updated_by = user
        super(Audit, self).save(*args, **kwargs)
