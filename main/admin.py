from django.utils.safestring import mark_safe
from projectCato.settings import constants as c


class AuditAdmin(object):
    readonly_fields = ('creation_date', 'created_by', 'updated_by',)
    fieldsets = ('creation_date', 'created_by', 'update_date', 'updated_by',)


def get_image_preview(obj, img, title, width=80, field_msg=c.PREVIEW_TEXT):
    if obj.pk:
        return mark_safe(f"""<a href="{img}" target="_blank">
        <img src="{img}" alt="{title}" style="max-width:{width}px; height: auto;" /></a>""")
    return field_msg


def _sect(sections, no_section):
    html = ""
    if sections:
        for section in sections:
            html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
    return no_section
