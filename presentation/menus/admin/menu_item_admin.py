from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from infrastructure.data_access.entities.menus.menu_item import MenuItem
from presentation import constants as c
from presentation.constants import NAME_KEY, MENU_KEY
from presentation.main.admin.filter_date_admin import FilterDateAdmin
from presentation.menus.inline.menu_item_language_inline import MenuItemLanguageInline


@admin.register(MenuItem)
class MenuItemAdmin(FilterDateAdmin, DraggableMPTTAdmin):
    __PARENT_KEY = "parent"
    __URL_KEY = "link"

    list_display = ('tree_actions', 'indented_title', __PARENT_KEY, MENU_KEY)
    expand_tree_by_default = True
    inlines = [MenuItemLanguageInline]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, __PARENT_KEY, MENU_KEY, __URL_KEY)
        }),
    )
    suit_form_tabs = (
        ('menu', c.MENU),
        ('language', c.LANGUAGE_TAB)
    )
