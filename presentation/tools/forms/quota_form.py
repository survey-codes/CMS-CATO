from django import forms

from domain.constants import TYPE_KEY
from domain.entities.tools.models.quota import Quota
from domain.exceptions.quota_exceptions import do_not_select_type_exception


class QuotaForm(forms.ModelForm):
    class Meta:
        model = Quota
        fields = "__all__"

    def clean_type(self):
        type_quota = self.cleaned_data.get(TYPE_KEY)
        if type_quota:
            return type_quota
        else:
            raise do_not_select_type_exception()
