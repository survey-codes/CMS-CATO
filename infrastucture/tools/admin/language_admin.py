from django.contrib import admin

from infrastucture.constants import LANGUAGE_TAB, NAME_KEY
from infrastucture.main.admin.audit_admin import AuditAdmin
from infrastucture.tools.models import Language


@admin.register(Language)
class LanguageAdmin(AuditAdmin):
    __ABBREVIATION = "abbreviation"

    fieldsets = (
        (LANGUAGE_TAB, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, __ABBREVIATION,)
        }),
    )
