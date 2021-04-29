from django import forms

from infrastructure.data_access.entities.tools.models import Mail


class SelectMailForm(forms.Form):
    mail = forms.ModelChoiceField(Mail.objects.all())
