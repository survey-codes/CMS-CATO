from django import forms

from infrastructure.data_access.entities.tools.models import Mail


class SelectMailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    mail = forms.ModelChoiceField(Mail.objects.all())
