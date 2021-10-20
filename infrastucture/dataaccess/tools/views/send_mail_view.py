from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from domain.exceptions.empty_template_exception import EmptyTemplateException
from domain.exceptions.invalid_form_exception import InvalidFromException
from domain.services.user_pqrd_service import UserPqrdService
from infrastucture.dataaccess.utilities.tasks.send_task import SendTask
from infrastucture.dataaccess.tools.models import UserPqrd
from infrastucture.constants import IDS, MAIL_KEY
from infrastucture.dataaccess.tools.forms.select_mail_form import SelectMailForm
from infrastucture.dataaccess.tools.views.base_view import BaseView


class SendMailView(BaseView):
    __USERS_KEY = "users"
    __user_pqrd_service = UserPqrdService()
    __send_task = SendTask()
    __request = None

    form_class = SelectMailForm
    initial = {'key': 'value'}
    template_name = "forms/select_mail.html"

    def __get_ids(self):
        return self.__request.GET.get(IDS)

    def __get_queryset(self):
        return self.__user_pqrd_service.select_by_list(self.__get_ids())

    def __render(self, form):
        return render(self.__request, self.template_name, context=dict(
            admin.site.each_context(self.__request),
            form=form,
            users=self.__get_queryset()
        ))

    @staticmethod
    def __reverse():
        user_pqrd = UserPqrd()
        return reverse(f'admin:{user_pqrd.get_app_label()}_{user_pqrd.get_model_name()}_changelist')

    def get(self, request, *args, **kwargs):
        self.__request = request
        form = self.form_class(initial=self.initial)
        return self.__render(form)

    def post(self, request, *args, **kwargs):
        self.__request = request
        form = self.form_class(request.POST)
        try:
            if not form.is_valid():
                raise InvalidFromException()
            mail = form.cleaned_data[MAIL_KEY]
            if not mail.template:
                raise EmptyTemplateException()
            users_pk = self.__get_queryset().values_list("pk")
            self.__send_task.mail(users_pk, mail.pk)
            return self.__render(form)
            # return HttpResponseRedirect(self.__reverse())
        except Exception as exception:
            messages.error(request, exception)
            return HttpResponseRedirect(request.get_full_path())
