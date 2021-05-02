from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.infrastructure.data_access.entities.main.audit import Audit
from cms.infrastructure.data_access.entities.tools.models import Language

CREATION_DATE_KEY = 'creation_date'
CREATED_BY_KEY = 'created_by'
UPDATE_DATE_KEY = 'update_date'
UPDATED_BY_KEY = 'updated_by'


class LanguageAbstract(Audit):
    """

    """
    __LANGUAGE_TAB = _('Languages')
    __LANGUAGE_MESSAGE = _('The same language should not be chosen more than once')

    language = models.ForeignKey(
        Language,
        verbose_name=__LANGUAGE_TAB,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True

    def unique_error_message(self, model_class, unique_check):
        return self.__LANGUAGE_MESSAGE
