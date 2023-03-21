from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from mptt.admin import DraggableMPTTAdmin

from infrastucture.constants import LANGUAGE_TAB, MENU_KEY, PARENT_KEY, TITLE_KEY, SLUG_KEY
from infrastucture.dataaccess.contents.admin.admin import SectionInline
from infrastucture.dataaccess.contents.inline.page_language_inline import PageLanguageInline
from infrastucture.dataaccess.contents.models import Page
from infrastucture.dataaccess.main.admin.filter_date_admin import FilterDateAdmin


@admin.register(Page)
class PageAdmin(FilterDateAdmin, DraggableMPTTAdmin):
    __PAGE = _('Page')
    __SECTION_PLURAL = _('Sections')
    __NO_SECTIONS = _("It does not contain sections")
    __TITLE = _("Title")

    DraggableMPTTAdmin.indented_title.short_description = __TITLE
    expand_tree_by_default = True
    list_display = ('tree_actions', 'indented_title', SLUG_KEY, '_show_sections')
    inlines = [SectionInline, PageLanguageInline]
    fieldsets = (
        (__PAGE, {
            'classes': ('suit-tab suit-tab-page',),
            'fields': (TITLE_KEY, PARENT_KEY, MENU_KEY, SLUG_KEY)
        }),
    )
    readonly_fields = (SLUG_KEY,)
    suit_form_tabs = (
        ('page', __PAGE),
        ('language', LANGUAGE_TAB),
        ('section', __SECTION_PLURAL),
    )

    def _show_sections(self, obj):
        sections = obj.sections.all()
        html = ""
        if sections.exists():
            for section in sections:
                html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
        return self.__NO_SECTIONS

    _show_sections.short_description = __SECTION_PLURAL

    def get_queryset(self, request):
        queryset = super(__class__, self).get_queryset(request)
        return queryset.annotate(section_count=Count('sections'))
