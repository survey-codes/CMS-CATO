from django import forms

from domain.constants import TYPE_KEY
from domain.entities.tools.models.quota import Quota
from domain.exceptions.quota_exceptions import DoNotSelectTypeException


class QuotaForm(forms.ModelForm):
    class Meta:
        model = Quota
        fields = "__all__"

    def clean_type(self):
        type_quota = self.cleaned_data.get(TYPE_KEY)
        if not type_quota:
            raise DoNotSelectTypeException()
        else:
            return type_quota
