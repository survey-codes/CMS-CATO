from django.contrib import admin
from django.urls import path
from django.utils.translation import ugettext_lazy as _

from infrastucture.constants import URL_MAIL
from infrastucture.dataaccess.tools.views.send_mail_view import SendMailView
from infrastucture.dataaccess.tools.admin.base_send_admin import BaseSendAdmin
from infrastucture.dataaccess.tools.forms.user_pqrd_form import EMAIL_KEY, UserPqrdForm
from infrastucture.dataaccess.tools.models import UserPqrd


@admin.register(UserPqrd)
class UserPqrdAdmin(BaseSendAdmin):
    __USER = _("User")
    list_display = (EMAIL_KEY,)
    search_fields = (EMAIL_KEY,)
    actions = ('mail_action',)

    form = UserPqrdForm
    readonly_fields = (EMAIL_KEY,)
    fieldsets = (
        (__USER, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (EMAIL_KEY,)
        }),
    )

    def get_urls(self):
        urls = super(UserPqrdAdmin, self).get_urls()
        new_urls = [
            path(URL_MAIL, SendMailView.as_view())
        ]
        return new_urls + urls
