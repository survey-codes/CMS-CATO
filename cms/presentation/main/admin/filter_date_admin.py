from rangefilter.filters import DateRangeFilter

from cms.presentation.main.admin.audit_admin import AuditAdmin


class FilterDateAdmin(AuditAdmin):
    __CREATION_DATE_KEY = 'creation_date'

    suit_list_filter_horizontal = (__CREATION_DATE_KEY,) + AuditAdmin.suit_list_filter_horizontal
    change_list_template = 'admin/change_date_filter.html'

    def get_list_filter(self, request):
        list_filter = super(FilterDateAdmin, self).get_list_filter(request)
        return ((self.__CREATION_DATE_KEY, DateRangeFilter),) + list_filter
