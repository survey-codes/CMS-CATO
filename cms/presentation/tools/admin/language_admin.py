from django.contrib import admin

from cms.infrastructure.data_access.entities.tools.models import Language
from cms.presentation.constants import LANGUAGE_TAB, NAME_KEY
from cms.presentation.main.admin.audit_admin import AuditAdmin


@admin.register(Language)
class LanguageAdmin(AuditAdmin):
    __ABBREVIATION = "abbreviation"

    fieldsets = (
        (LANGUAGE_TAB, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (NAME_KEY, __ABBREVIATION,)
        }),
    )
