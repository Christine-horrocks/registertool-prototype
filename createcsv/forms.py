from django import forms
from django.forms import ModelForm
from .models import LocalPlans, DeveloperContributions

from datetime import datetime

class PickModel(forms.Form):
    category = forms.ChoiceField(choices=[('localplans', 'Local Plans'), ('developercontributions', 'Developer Contributions'), ('stuffwithtrees', 'Stuff with Trees')])

class LocalPlansForm(forms.ModelForm):
    entrydate =  forms.DateField(error_messages={'required': "Incorrect data format, should be YYYY-MM-DD"})
    class Meta:
        model = LocalPlans
        fields = ['name', 'organisation', 'entrydate', 'state']

class DeveloperContribuationsForm(forms.ModelForm):
    entrydate =  forms.DateField(error_messages={'required': "Incorrect data format, should be YYYY-MM-DD"})
    the_lovely_things_we_will_get = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = DeveloperContributions
        widgets = {
            'developer_name': forms.TextInput(attrs= {'class': 'govuk-input'})
        }
        fields = ['developer_name', 'local_authoriy_name', 'entrydate', 'the_lovely_things_we_will_get']