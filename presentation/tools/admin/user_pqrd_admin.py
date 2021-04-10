from django.contrib import admin

from domain.entities.tools.models.user_pqrd import UserPqrd, USER
from presentation.tools.admin.base_send_admin import BaseSendAdmin
from presentation.tools.forms.user_pqrd_form import EMAIL_KEY, UserPqrdForm


@admin.register(UserPqrd)
class UserPqrdAdmin(BaseSendAdmin):
    form = UserPqrdForm
    list_display = (EMAIL_KEY,)
    readonly_fields = (EMAIL_KEY,)
    fieldsets = (
        (USER, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (EMAIL_KEY,)
        }),
    )
    search_fields = (EMAIL_KEY,)
    actions = ('mail_action',)
