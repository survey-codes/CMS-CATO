from infrastructure.data_access.entities.main.language_abstract import CREATION_DATE_KEY, UPDATE_DATE_KEY
from presentation.constants import ACTIVE_KEY, AUDIT, CREATED_BY_KEY, UPDATED_BY_KEY
from presentation.main.admin.base_admin import BaseAdmin


class AuditAdmin(BaseAdmin):
    __CREATED_BY_USERNAME_KEY = 'created_by__username'
    __UPDATED_BY_USERNAME_KEY = 'updated_by__username'

    suit_list_filter_horizontal = (ACTIVE_KEY,)

    __fieldsets_default = (
        (AUDIT, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (ACTIVE_KEY, (CREATED_BY_KEY, CREATION_DATE_KEY), (UPDATED_BY_KEY, UPDATE_DATE_KEY),)
        }),
    )

    def get_search_fields(self, request):
        search_fields = (self.__CREATED_BY_USERNAME_KEY, self.__UPDATED_BY_USERNAME_KEY)
        return self.search_fields + search_fields

    def get_list_filter(self, request):
        list_filter = (ACTIVE_KEY,)
        return self.list_filter + list_filter

    def get_list_display(self, request):
        list_display = (ACTIVE_KEY,)
        return self.list_display + list_display

    def get_list_display_links(self, request, list_display):
        return list_display

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = (CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY,)
        return self.readonly_fields + readonly_fields

    def get_fieldsets(self, request, obj=None):
        return self.fieldsets + self.__fieldsets_default
