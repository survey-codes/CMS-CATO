from django.contrib import admin, messages
from django.contrib.admin import register
from rangefilter.filter import DateRangeFilter

from presentation.main.admin import AuditAdmin, CREATION_DATE_KEY
from presentation.menus.models import Menu, MenuItem, MenuItemLanguage, MenuLanguage
from projectCato.settings import constants as c

NAME_KEY = "name"
GENERAL_KEY = "general"
SHORT_DESCRIPTION_UPDATE_JSON_CONTENT = "Update json content"


class MenuLanguageInline(admin.TabularInline):
    model = MenuLanguage
    extra = 0
    suit_classes = 'suit-tab suit-tab-language'


@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (NAME_KEY, GENERAL_KEY)
    actions = ['update_json_content']
    search_fields = (CREATION_DATE_KEY,)
    list_filter = ((CREATION_DATE_KEY, DateRangeFilter),)
    suit_list_filter_horizontal = (CREATION_DATE_KEY,)
    change_list_template = 'admin/change_date_filter.html'
    readonly_fields = AuditAdmin.readonly_fields
    inlines = [MenuLanguageInline]
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, GENERAL_KEY,) + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('menu', c.MENU),
        ('language', c.LANGUAGE_TAB)
    )

    def update_json_content(self, request, queryset):
        from domain.menus.utils import update_json_content_menu
        for menu in queryset:
            update_json_content_menu(menu)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = SHORT_DESCRIPTION_UPDATE_JSON_CONTENT


class MenuItemLanguageInline(admin.StackedInline):
    model = MenuItemLanguage
    extra = 0
    suit_classes = 'suit-tab suit-tab-language'


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    actions = ['update_json_content']
    search_fields = ('creation_date',)
    list_filter = (('creation_date', DateRangeFilter),)
    suit_list_filter_horizontal = ('creation_date',)
    change_list_template = 'admin/change_date_filter.html'
    inlines = [MenuItemLanguageInline]
    readonly_fields = AuditAdmin.readonly_fields
    fieldsets = (
        (None, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': ('name', 'parent', 'menu', 'url', 'page_url', 'slug_url',) + AuditAdmin.fieldsets
        }),
    )

    suit_form_tabs = (
        ('menu', c.MENU),
        ('language', c.LANGUAGE_TAB)
    )

    def update_json_content(self, request, queryset):
        from domain.menus.utils import update_json_content_menu_item
        for menu_item in queryset:
            update_json_content_menu_item(menu_item)

        self.message_user(
            request,
            c.JSON_UPDATE_MESSAGE, messages.SUCCESS
        )
        return True

    update_json_content.short_description = "Actualizar contenido JSON"
