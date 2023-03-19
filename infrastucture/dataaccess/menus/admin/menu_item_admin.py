from django.contrib import admin
from django.db.models import F
from django.utils.translation import ugettext_lazy as _
from mptt.admin import DraggableMPTTAdmin

from infrastucture.constants import NAME_KEY, MENU_KEY, MENU, LANGUAGE_TAB, PARENT_KEY
from infrastucture.dataaccess.main.admin.filter_date_admin import FilterDateAdmin
from infrastucture.dataaccess.menus.inline.menu_item_language_inline import MenuItemLanguageInline
from infrastucture.dataaccess.menus.models.menu_item import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(FilterDateAdmin, DraggableMPTTAdmin):
    __URL_KEY = "link"
    __PARENT_NAME_KEY = "parent__name"
    __PARENT = _("Parent")

    list_display = ('tree_actions', 'indented_title', "_get_parent_name", MENU_KEY)
    expand_tree_by_default = True
    inlines = [MenuItemLanguageInline]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, PARENT_KEY, MENU_KEY, __URL_KEY)
        }),
    )
    suit_form_tabs = (
        ('menu', MENU),
        ('language', LANGUAGE_TAB)
    )

    def _get_parent_name(self, obj: MenuItem):
        return obj.parent_name

    _get_parent_name.short_description = __PARENT
    _get_parent_name.admin_order_field = __PARENT_NAME_KEY

    def get_queryset(self, request):
        queryset: 'Queryet[MenuItem]' = super(MenuItemAdmin, self).get_queryset(request)
        return queryset.annotate(parent_name=F(self.__PARENT_NAME_KEY))
