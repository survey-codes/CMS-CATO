from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from infrastucture.dataaccess.tools.models import Template
from infrastucture.constants import NAME_KEY
from infrastucture.dataaccess.main.admin.audit_admin import AuditAdmin


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
