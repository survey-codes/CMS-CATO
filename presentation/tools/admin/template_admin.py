from django.contrib import admin

from infrastructure.data_access.entities.tools.models.template import Template, TEMPLATES, TEMPLATE_ID_KEY
from presentation.constants import NAME_KEY
from presentation.main.admin.audit_admin import AuditAdmin


@admin.register(Template)
class TemplateAdmin(AuditAdmin):
    list_display = (NAME_KEY,)
    fieldsets = (
        (TEMPLATES, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, TEMPLATE_ID_KEY,)
        }),
    )
