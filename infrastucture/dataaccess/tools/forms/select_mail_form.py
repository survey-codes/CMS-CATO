from django import forms

from infrastucture.dataaccess.tools.models import Mail


class SelectMailForm(forms.Form):
    mail = forms.ModelChoiceField(Mail.objects.all())
