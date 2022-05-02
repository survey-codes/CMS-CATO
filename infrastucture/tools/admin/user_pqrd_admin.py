from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.translation import ugettext_lazy as _

from domain.main.exceptions.empty_mail_exception import EmptyMailException
from domain.main.exceptions.zero_active_users_exception import ZeroActiveUsersException
from domain.main.exceptions.zero_quota_exception import ZeroQuotaException
from infrastucture.constants import URL_MAIL, IDS
from infrastucture.main.admin.read_only_base_admin import ReadOnlyBaseAdmin
from infrastucture.tools.forms.user_pqrd_form import EMAIL_KEY, UserPqrdForm
from infrastucture.tools.models import UserPqrd
from infrastucture.tools.models.quota_type import QuotaType
from infrastucture.tools.repository.mail_repository_impl import MailRepositoryImpl
from infrastucture.tools.repository.quota_repository_impl import QuotaRepositoryImpl
from infrastucture.tools.repository.user_pqrd_repository_impl import UserPqrdRepositoryImpl
from infrastucture.tools.views.send_mail_view import SendMailView

SEND_MAIL = _("Send mail")
MAIL_SHORT_DESCRIPTION = "Enviar correo electrónico"
INITIAL_FORM = "_selected_action"
APPLY = "apply"
MAIL_ACTION_KEY = "mail_action"


class BaseSendAdmin(ReadOnlyBaseAdmin):
    __queryset = None
    __quota_repository = QuotaRepositoryImpl()
    __mail_repository = MailRepositoryImpl()
    __user_pqrd_repository = UserPqrdRepositoryImpl()

    def mail_action(self, request, queryset):
        self.__queryset = queryset
        if not self.__quota_repository.haveQuotaByType(QuotaType.MAIL):
            raise ZeroQuotaException()
        return self.__validate_mail_template()

    mail_action.short_description = MAIL_SHORT_DESCRIPTION

    def __validate_mail_template(self):
        if self.__mail_repository.isEmpty():
            raise EmptyMailException()
        return self.__validate_active_users()

    def __validate_active_users(self):
        if not self.__user_pqrd_repository.there_are_active_users():
            raise ZeroActiveUsersException()
        return HttpResponseRedirect(f"{URL_MAIL}?{IDS}={self.__get_ids()}")

    def __get_ids(self):
        selected = self.__queryset.values_list('pk', flat=True)
        return ",".join(str(pk) for pk in selected)

    def get_urls(self):
        urls = super(BaseSendAdmin, self).get_urls()
        new_urls = [
            path(URL_MAIL, SendMailView.as_view())
        ]
        return new_urls + urls

    # quota_repository = QuotaRepositoryImpl()
    # mail_repository = MailRepositoryImpl()
    # user_pqrd_service = UserPqrdServiceBorrador()
    # queryset = None
    #
    # @staticmethod
    # def __get_mail_select_form(request):
    #     return SelectMailForm(initial={INITIAL_FORM: request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
    #
    # @staticmethod
    # def __render_form(request, form, users):
    #     return render(request, "forms/select_mail.html", context=dict(
    #         admin.site.each_context(request),
    #         form=form,
    #         users=users,
    #         name=APPLY,
    #         action=MAIL_ACTION_KEY
    #     ))
    #
    # @staticmethod
    # def __get_form_by_button(request):
    #     if APPLY in request.POST:
    #         return SelectMailForm(request.POST)
    #
    # @staticmethod
    # def __send_mail_to_users(users, mail):
    #     response_user_send = ResponseUserSend()
    #     for user in users:
    #         # Llevar a celery el envio
    #         response_user_send.plus_one_successful_amount()
    #         print(user)
    #     return response_user_send
    #
    # @staticmethod
    # def __update_number_of_shipments(mail, amount_success):
    #     mail.add_to_amount_send(amount_success)
    #     mail.save()
    #
    # @staticmethod
    # def __update_quota(quota, amount_success):
    #     quota.subtract_quota(amount_success)
    #     quota.save()
    #
    # def __get_ids(self):
    #     selected = self.queryset.values_list('pk', flat=True)
    #     return ",".join(str(pk) for pk in selected)
    #
    # def __validate_active_users(self):
    #     users = self.queryset.filter(active=DEFAULT_BOOL)
    #     if not users:
    #         raise ZeroActiveUsersException()
    #     return HttpResponseRedirect(f"{URL_MAIL}?{IDS}={self.__get_ids()}")
    #
    # def __validate_that_there_are_mails(self):
    #     isEmpty = self.mail_repository.isEmpty()
    #     if isEmpty:
    #         raise EmptyMailException()
    #     return self.__validate_active_users()
    #
    # def mail_action(self, request, queryset):
    #     self.queryset = queryset
    #     quota = self.quota_repository.select()
    #     if not quota or quota.zero_quota:
    #         raise ZeroQuotaException()
    #     return self.__validate_that_there_are_mails()
    #
    # mail_action.short_description = MAIL_SHORT_DESCRIPTION


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
