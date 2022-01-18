from django import forms

from domain.main.exceptions.user_pqrd_exceptions import do_not_write_email_exception
from infrastucture.tools.models import UserPqrd

EMAIL_KEY = "email"


class UserPqrdForm(forms.ModelForm):
    class Meta:
        model = UserPqrd
        fields = "__all__"

    def clean_email(self):
        email = self.cleaned_data.get(EMAIL_KEY)
        if email:
            return email
        else:
            raise do_not_write_email_exception()
