from django.contrib import admin

from cms.infrastructure.data_access.entities.tools.models import Mail
from cms.presentation.constants import NAME_KEY, MAIL
from cms.presentation.main.admin.audit_admin import AuditAdmin


@admin.register(Mail)
class MailAdmin(AuditAdmin):
    __AMOUNT_SEND_KEY = "amount_send"
    __TEMPLATE_KEY = "template"

    list_display = (NAME_KEY, __TEMPLATE_KEY, __AMOUNT_SEND_KEY,)

    fieldsets = (
        (MAIL, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': ((NAME_KEY, __TEMPLATE_KEY), __AMOUNT_SEND_KEY)
        }),
    )
    readonly_fields = (__AMOUNT_SEND_KEY,)
