from django.utils.translation import ugettext_lazy as _

from domain.constants import ACTIVE_KEY
from domain.entities.main.models import CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY
from presentation.main.admin.base_admin import BaseAdmin

AUDIT = _("Audit")


class AuditAdmin(BaseAdmin):
    list_display_default = (ACTIVE_KEY,)
    readonly_fields_default = (CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY,)
    fieldsets_default = (
        (AUDIT, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (ACTIVE_KEY, (CREATED_BY_KEY, CREATION_DATE_KEY), (UPDATED_BY_KEY, UPDATE_DATE_KEY),)
        }),
    )
    list_filter_default = (ACTIVE_KEY,)

    def get_list_filter(self, request):
        if self.list_filter:
            return self.list_filter + self.list_filter_default
        return self.list_filter_default

    def get_list_display(self, request):
        if self.list_display:
            return self.list_display + self.list_display_default
        return self.list_display

    def get_readonly_fields(self, request, obj=None):
        if self.readonly_fields:
            return self.readonly_fields + self.readonly_fields_default
        return self.readonly_fields_default

    def get_fieldsets(self, request, obj=None):
        if self.fieldsets:
            return self.fieldsets + self.fieldsets_default
        return self.fieldsets_default
