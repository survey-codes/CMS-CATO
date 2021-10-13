from django.contrib import admin

from infrastucture.dataaccess.menus.models.menu import Menu
from infrastucture.constants import NAME_KEY, LANGUAGE_TAB, MENU
from infrastucture.dataaccess.main.admin.filter_date_admin import FilterDateAdmin
from infrastucture.dataaccess.menus.inline.menu_language_inline import MenuLanguageInline


@admin.register(Menu)
class MenuAdmin(FilterDateAdmin):
    __GENERAL_KEY = "is_general"

    list_display = (NAME_KEY, __GENERAL_KEY)
    search_fields = (NAME_KEY,)
    list_filter = (__GENERAL_KEY,)
    suit_list_filter_horizontal = (__GENERAL_KEY,) + FilterDateAdmin.suit_list_filter_horizontal
    inlines = [MenuLanguageInline]
    fieldsets = (
        (MENU, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, __GENERAL_KEY)
        }),
    )
    suit_form_tabs = (
        ('menu', MENU),
        ('language', LANGUAGE_TAB)
    )
