from django.contrib import admin

from domain.entities.tools.models.template import Template, TEMPLATES, TEMPLATE_ID_KEY
from presentation.main.admin.audit_admin import AuditAdmin
from presentation.menus.admin import NAME_KEY


@admin.register(Template)
class TemplateAdmin(AuditAdmin):
    fieldsets = (
        (TEMPLATES, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, TEMPLATE_ID_KEY,)
        }),
    )
