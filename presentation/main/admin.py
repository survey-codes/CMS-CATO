from django.utils.safestring import mark_safe

from domain.main.models import CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY


class AuditAdmin:
    readonly_fields = ('creation_date', 'created_by', 'update_date', 'updated_by')
    fieldsets = (('created_by', 'creation_date'), ('updated_by', 'update_date'),)


def _sect(sections, no_section):
    html = ""
    if sections:
        for section in sections:
            html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
    return no_section
