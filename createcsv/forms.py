from django import forms
from django.forms import ModelForm
from .models import LocalPlans

# class CreateCsvForm(forms.Form):
#     # name = forms.CharField()
#     # email = forms.EmailField(label='E-mail')
#     # category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
#     # subject = forms.CharField(required=False)
#     # body = forms.CharField(widget=forms.Textarea)
#     register = forms.CharField()
#     headers = forms.CharField(widget=forms.Textarea)

class CreateCsvForm(ModelForm):
    class Meta:
        model = LocalPlans
        fields = ['name', 'organisation', 'entrydate', 'state']

form =CreateCsvForm()



class UpdateCsvForm(forms.Form):
    # register = forms.CharField()

    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(UpdateCsvForm, self).__init__(*args, **kwargs)

        for i, heading in enumerate(extra):
            self.fields['custom_%s' % i] = forms.CharField(label=heading)