from django.contrib import admin

from domain.menus.models import Menu, MenuItem, MenuItemLanguage, MenuLanguage
from presentation import constants as c
from presentation.main.admin import AuditAdmin, CREATION_DATE_KEY
from rangefilter.filter import DateRangeFilter


NAME_KEY = "name"
GENERAL_KEY = "is_general"
PARENT_KEY = "parent"
MENU_KEY = "menu"
URL_KEY = "link"


#---------INLINES---------
class MenuLanguageInline(admin.StackedInline):
    model = MenuLanguage
    extra = 1
    suit_classes = 'suit-tab suit-tab-language'


class MenuItemLanguageInline(admin.StackedInline):
    model = MenuItemLanguage
    extra = 1
    suit_classes = 'suit-tab suit-tab-language'


#---------ADMIN---------
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (NAME_KEY, GENERAL_KEY)
    search_fields = (CREATION_DATE_KEY,)
    list_filter = ((CREATION_DATE_KEY, DateRangeFilter),)
    suit_list_filter_horizontal = (CREATION_DATE_KEY,)
    change_list_template = 'admin/change_date_filter.html'
    readonly_fields = AuditAdmin.readonly_fields
    inlines = [MenuLanguageInline]
    fieldsets = (
        ('Menu', {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, GENERAL_KEY) + AuditAdmin.fieldsets
        }),
    )
    suit_form_tabs = (
        ('menu', c.MENU),
        ('language', c.LANGUAGE_TAB)
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    search_fields = (CREATION_DATE_KEY,)
    list_filter = ((CREATION_DATE_KEY, DateRangeFilter),)
    suit_list_filter_horizontal = (CREATION_DATE_KEY,)
    change_list_template = 'admin/change_date_filter.html'
    inlines = [MenuItemLanguageInline]
    readonly_fields = AuditAdmin.readonly_fields
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, PARENT_KEY, MENU_KEY, URL_KEY) + AuditAdmin.fieldsets
        }),
    )
    suit_form_tabs = (
        ('menu', c.MENU),
        ('language', c.LANGUAGE_TAB)
    )
