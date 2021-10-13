from django.contrib import admin
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from infrastucture.dataaccess.tools.models import Quota
from infrastucture.constants import MAIL_KEY
from infrastucture.dataaccess.main.admin.audit_admin import AuditAdmin
from infrastucture.dataaccess.tools.forms.quota_form import QuotaForm


@admin.register(Quota)
class QuotaAdmin(AuditAdmin):
    __QUOTA = _("Quota")
    __CONTINUE_KEY = "_continue"
    __ADD_OTHER_KEY = "_addanother"
    __AMOUNT_KEY = "amount"
    __MAIL = _("Mail")
    __SMS = _("Sms")
    __SMS_KEY = "sms"
    __TYPE_CHOICES = (
        (MAIL_KEY, __MAIL),
        (__SMS_KEY, __SMS)
    )
    __TYPE_KEY = "type"

    list_display = (__TYPE_KEY, __AMOUNT_KEY)
    list_display_links = list_display
    form = QuotaForm
    fieldsets = (
        (__QUOTA, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': ((__AMOUNT_KEY, __TYPE_KEY),)
        }),
    )

    def __is_less(self):
        return self.model.objects.count() < len(self.__TYPE_CHOICES)

    def redirect_to_model_list(self, request, pk):
        # Esto debe cambiar para que se haga automatico y no este acoplado
        if self.__is_less():
            if self.__CONTINUE_KEY in request.POST:
                return redirect(f"/admin/tools/quota/{pk}/change")
            elif self.__ADD_OTHER_KEY in request.POST:
                return redirect("/admin/tools/quota/add")
        return redirect("/admin/tools/quota")

    def has_add_permission(self, request):
        return self.__is_less()

    def response_add(self, request, obj, post_url_continue=None):
        return self.redirect_to_model_list(request, obj.pk)

    def response_change(self, request, obj):
        return self.redirect_to_model_list(request, obj.pk)
