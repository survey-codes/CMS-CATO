from django.contrib import admin, messages
from django.http import HttpResponseRedirect


class BaseAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        try:
            return super(BaseAdmin, self).changelist_view(request, extra_context)
        except Exception as exception:
            self.show_error_message(request, exception)
            return HttpResponseRedirect(request.path)

    def show_error_message(self, request, message):
        self.message_user(request, message, messages.ERROR)

    def show_warning_message(self, request, message):
        self.message_user(request, message, messages.WARNING)

    def show_success_message(self, request, message):
        self.message_user(request, message, messages.SUCCESS)