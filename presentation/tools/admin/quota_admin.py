from django.contrib import admin
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from domain.constants import TYPE_KEY
from domain.entities.tools.models.quota import Quota, AMOUNT_KEY, TYPE_CHOICES
from presentation.main.admin.audit_admin import AuditAdmin
from presentation.tools.forms.quota_form import QuotaForm

QUOTA = _("Quota")


@admin.register(Quota)
class QuotaAdmin(AuditAdmin):
    list_display = (TYPE_KEY, AMOUNT_KEY)
    list_display_links = list_display
    form = QuotaForm
    fieldsets = (
        (QUOTA, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': ((AMOUNT_KEY, TYPE_KEY),)
        }),
    )

    def is_less(self):
        return self.model.objects.count() < len(TYPE_CHOICES)

    def redirect_to_model_list(self):
        # Esto debe cambiar para que se haga automatico y no este acoplado
        if not self.is_less():
            return redirect("/admin/tools/quota")

    def has_add_permission(self, request):
        return self.is_less()

    def response_add(self, request, obj, post_url_continue=None):
        return self.redirect_to_model_list()

    def response_change(self, request, obj):
        return self.redirect_to_model_list()

