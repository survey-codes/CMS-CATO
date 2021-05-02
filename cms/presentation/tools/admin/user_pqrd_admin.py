from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from infrastructure.data_access.entities.tools.models.user_pqrd import UserPqrd
from presentation.tools.admin.base_send_admin import BaseSendAdmin
from presentation.tools.forms.user_pqrd_form import EMAIL_KEY, UserPqrdForm


@admin.register(UserPqrd)
class UserPqrdAdmin(BaseSendAdmin):
    __USER = _("User")
    list_display = (EMAIL_KEY,)
    search_fields = (EMAIL_KEY,)
    actions = ('mail_action', 'export_selected_objects')

    form = UserPqrdForm
    readonly_fields = (EMAIL_KEY,)
    fieldsets = (
        (__USER, {
            'classes': ('suit-tab suit-tab-menu',),
            'fields': (EMAIL_KEY,)
        }),
    )
