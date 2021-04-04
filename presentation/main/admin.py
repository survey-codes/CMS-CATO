from django.utils.safestring import mark_safe


class AuditAdmin(object):
    readonly_fields = ('creation_date', 'created_by', 'update_date', 'updated_by',)
    fieldsets = ('creation_date', 'created_by', 'update_date', 'updated_by',)


def _sect(sections, no_section):
    html = ""
    if sections:
        for section in sections:
            html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
    return no_section
