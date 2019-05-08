from django import forms
from django.forms import ModelForm
from .models import LocalPlans

class PickModel(forms.Form):
    category = forms.ChoiceField(choices=[('localplans', 'Local Plans'), ('developercontributions', 'Developer Contributions'), ('stuffwithtrees', 'Stuff with Trees')])

class LocalPlansForm(ModelForm):
    class Meta:
        model = LocalPlans
        fields = ['name', 'organisation', 'entrydate', 'state']