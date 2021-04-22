from django.utils.translation import ugettext_lazy as _

from domain.constants import ACTIVE_KEY
from infrastructure.data_access.entities.main.models import CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, \
    UPDATED_BY_KEY
from presentation.main.admin.base_admin import BaseAdmin

AUDIT = _("Audit")


class AuditAdmin(BaseAdmin):
    __list_display_default = (ACTIVE_KEY,)
    __list_filter_default = (ACTIVE_KEY,)
    suit_list_filter_horizontal = (ACTIVE_KEY,)
    __search_fields_default = (CREATED_BY_KEY, UPDATED_BY_KEY)

    __fieldsets_default = (
        (AUDIT, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (ACTIVE_KEY, (CREATED_BY_KEY, CREATION_DATE_KEY), (UPDATED_BY_KEY, UPDATE_DATE_KEY),)
        }),
    )
    __readonly_fields_default = (CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY,)

    def get_search_fields(self, request):
        if self.search_fields:
            return self.search_fields + self.__search_fields_default
        return self.__search_fields_default

    def get_list_filter(self, request):
        if self.list_filter:
            return self.list_filter + self.__list_filter_default
        return self.__list_filter_default

    def get_list_display(self, request):
        if self.list_display:
            return self.list_display + self.__list_display_default
        return self.list_display

    def get_list_display_links(self, request, list_display):
        return list_display

    def get_readonly_fields(self, request, obj=None):
        if self.readonly_fields:
            return self.readonly_fields + self.__readonly_fields_default
        return self.__readonly_fields_default

    def get_fieldsets(self, request, obj=None):
        if self.fieldsets:
            return self.fieldsets + self.__fieldsets_default
        return self.__fieldsets_default
