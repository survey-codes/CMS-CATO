from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from infrastucture.constants import NAME_KEY
from infrastucture.main.admin.audit_admin import AuditAdmin
from infrastucture.tools.models import Template


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
