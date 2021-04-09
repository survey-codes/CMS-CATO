from django.contrib import admin

from domain.entities.tools.models.template import Template
from presentation.main.admin.audit_admin import AuditAdmin


@admin.register(Template)
class TemplateAdmin(AuditAdmin):
    pass
