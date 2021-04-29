from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from domain.services.user_pqrd_service import UserPqrdService
from infrastructure.data_access.entities.tools.models import UserPqrd
from presentation.constants import IDS
from presentation.tools.forms.select_mail_form import SelectMailForm
from presentation.tools.views.base_view import BaseView


class SendMailView(BaseView):
    __user_pqrd_service = UserPqrdService()
    __request = None

    form_class = SelectMailForm
    initial = {'key': 'value'}
    template_name = "forms/select_mail.html"

    def __render(self, form, ids=str()):
        return render(self.__request, self.template_name, context=dict(
            admin.site.each_context(self.__request),
            form=form,
            users=self.__user_pqrd_service.select_by_list(ids)
        ))

    @staticmethod
    def __reverse():
        user_pqrd = UserPqrd()
        return reverse(f'admin:{user_pqrd.get_app_label()}_{user_pqrd.get_model_name()}_changelist')

    def get(self, request, *args, **kwargs):
        self.__request = request
        form = self.form_class(initial=self.initial)
        ids = self.__get_ids()
        return self.__render(form, ids)

    def __get_ids(self):
        return self.__request.GET.get(IDS)

    def post(self, request, *args, **kwargs):
        self.__request = request
        form = self.form_class(request.POST)
        try:
            ids = str()
            if form.is_valid():
                ids = self.__get_ids()
                # return HttpResponseRedirect(self.__reverse())
            return self.__render(form, ids)
        except Exception as exception:
            messages.error(request, exception)
            return HttpResponseRedirect(request.get_full_path())
