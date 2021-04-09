from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from domain.entities.response_user_send import ResponseUserSend
from domain.entities.tools.models import Quota
from domain.exceptions.empty_template_exceltion import EmptyTemplateException
from domain.exceptions.invalid_form_exception import InvalidFromException
from domain.exceptions.zero_active_users_exception import ZeroActiveUsersException
from domain.exceptions.zero_quota_exception import ZeroQuotaException
from presentation.constants import MAIL_KEY
from presentation.main.admin.read_only_base_admin import ReadOnlyBaseAdmin
from presentation.tools.forms.select_mail_form import SelectMailForm

SEND_MAIL = _("Send mail")
MAIL_SHORT_DESCRIPTION = "Enviar correo electrónico"
INITIAL_FORM = "_selected_action"
APPLY = "apply"
MAIL_ACTION_KEY = "mail_action"


class BaseSendAdmin(ReadOnlyBaseAdmin):

    @staticmethod
    def __get_mail_select_form(request):
        return SelectMailForm(initial={INITIAL_FORM: request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

    @staticmethod
    def __render_form(request, form, users):
        return render(request, "forms/select_mail.html", context=dict(
            admin.site.each_context(request),
            form=form,
            users=users,
            name=APPLY,
            action=MAIL_ACTION_KEY
        ))

    @staticmethod
    def __get_form_by_button(request):
        if APPLY in request.POST:
            return SelectMailForm(request.POST)

    @staticmethod
    def __get_selected_mail(form):
        return form.cleaned_data[MAIL_KEY]

    @staticmethod
    def __send_mail_to_users(users, mail):
        response_user_send = ResponseUserSend()
        for user in users:
            # Llevar a celery el envio
            response_user_send.plus_one_successful_amount()
            print(user)
        return response_user_send

    @staticmethod
    def __update_number_of_shipments(mail, amount_success):
        mail.add_to_amount_send(amount_success)
        mail.save()

    @staticmethod
    def __update_quota(quota, amount_success):
        quota.subtract_quota(amount_success)
        quota.save()

    def __validate_active_users(self, request, queryset, quota):
        users = queryset.filter(active=True)
        if not users:
            raise ZeroActiveUsersException()
        else:
            form = self.__get_form_by_button(request)
            if not form:
                form = self.__get_mail_select_form(request)
            elif form.is_valid():
                mail = self.__get_selected_mail(form)
                if mail.empty_template:
                    self.show_error_message(request, EmptyTemplateException())
                else:
                    response_send = self.__send_mail_to_users(users, mail)
                    if response_send.has_failed_users():
                        self.show_warning_message(request, response_send.message_failed_shipment())
                        form = self.__get_mail_select_form(request)
                    else:
                        self.show_success_message(request, response_send.message_successful_shipment())
                        self.__update_number_of_shipments(mail, response_send.successful_amount)
                        self.__update_quota(quota, response_send.successful_amount)
                        return HttpResponseRedirect(request.get_full_path())
            else:
                raise InvalidFromException()
            return self.__render_form(request, form, users)

    def mail_action(self, request, queryset):
        quota = Quota.objects.filter(type=MAIL_KEY).first()
        if quota.zero_quota:
            raise ZeroQuotaException()
        else:
            return self.__validate_active_users(request, queryset, quota)

    mail_action.short_description = MAIL_SHORT_DESCRIPTION
