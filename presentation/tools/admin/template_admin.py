from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from infrastructure.data_access.entities.tools.models.template import Template
from presentation.constants import NAME_KEY
from presentation.main.admin.audit_admin import AuditAdmin


@admin.register(Template)
class TemplateAdmin(AuditAdmin):
    __TEMPLATE_ID_KEY = "template_id"
    __TEMPLATES = _("Templates")

    list_display = (NAME_KEY,)
    fieldsets = (
        (__TEMPLATES, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, __TEMPLATE_ID_KEY,)
        }),
    )
