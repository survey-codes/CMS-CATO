from django.contrib import admin, messages
from django.http import HttpResponseRedirect

from infrastucture.constants import EMPTY_VALUE
from infrastucture.main.admin.base import Base


class BaseAdmin(admin.ModelAdmin, Base):
    empty_value_display = EMPTY_VALUE

    def changelist_view(self, request, extra_context=None):
        try:
            return super(BaseAdmin, self).changelist_view(request, extra_context)
        except Exception as exception:
            self.show_error_message(request, exception)
            return HttpResponseRedirect(request.get_full_path())

    def show_error_message(self, request, message):
        self.message_user(request, message, messages.ERROR)

    def show_warning_message(self, request, message):
        self.message_user(request, message, messages.WARNING)

    def show_success_message(self, request, message):
        self.message_user(request, message, messages.SUCCESS)
