from django import forms

from domain.entities.tools.models import Mail


class SelectMailForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    mail = forms.ModelChoiceField(Mail.objects.all())
