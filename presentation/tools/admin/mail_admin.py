from django.contrib import admin

from domain.constants import NAME_KEY
from domain.entities.tools.models import Mail
from domain.entities.tools.models.mail import MAIL
from presentation.main.admin.audit_admin import AuditAdmin

AMOUNT_SEND_KEY = "amount_send"
TEMPLATE_KEY = "template"


@admin.register(Mail)
class MailAdmin(AuditAdmin):
    readonly_fields = (AMOUNT_SEND_KEY,)
    fieldsets = (
        (MAIL, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': ((NAME_KEY, TEMPLATE_KEY), AMOUNT_SEND_KEY)
        }),
    )
