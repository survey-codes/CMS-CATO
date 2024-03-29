from django import forms

from domain.main.exceptions.quota_exceptions import DoNotSelectTypeException
from infrastucture.dataaccess.tools.models import Quota


class QuotaForm(forms.ModelForm):
    __TYPE_KEY = "type"

    class Meta:
        model = Quota
        fields = "__all__"

    def clean_type(self):
        type_quota = self.cleaned_data.get(self.__TYPE_KEY)
        if not type_quota:
            raise DoNotSelectTypeException()
        else:
            return type_quota
