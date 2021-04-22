from infrastructure.data_access.entities.main.language_abstract import CREATION_DATE_KEY, UPDATE_DATE_KEY
from presentation.constants import CREATED_BY_KEY, UPDATED_BY_KEY, ACTIVE_KEY
from presentation.main.inline.base_inline import BaseInline


class AuditInline(BaseInline):

    def get_fields(self, request, obj=None):
        return ACTIVE_KEY, (CREATED_BY_KEY, CREATION_DATE_KEY), (UPDATED_BY_KEY, UPDATE_DATE_KEY),

    def get_readonly_fields(self, request, obj=None):
        return CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY,
