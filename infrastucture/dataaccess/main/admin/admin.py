from django.utils.safestring import mark_safe

from infrastucture.dataaccess.main.models.language_abstract import CREATION_DATE_KEY, CREATED_BY_KEY, \
    UPDATE_DATE_KEY, UPDATED_BY_KEY


class Audit2Admin(object):
    readonly_fields = (CREATION_DATE_KEY, CREATED_BY_KEY, UPDATE_DATE_KEY, UPDATED_BY_KEY,)
    fieldsets = ((CREATED_BY_KEY, CREATION_DATE_KEY), (UPDATED_BY_KEY, UPDATE_DATE_KEY),)


def _sect(sections, no_section):
    html = ""
    if sections:
        for section in sections:
            html += f'<li><a href="/admin/contents/section/{section.id}/">{section}</a></li>'
            return mark_safe(f'<ul>{html}</ul>')
    return no_section
