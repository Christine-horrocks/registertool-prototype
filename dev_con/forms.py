from django import forms
from django.shortcuts import render

class PickCsvForm(forms.Form):
    category = forms.ChoiceField(choices=[('developer-agreement-contributions', 'Developer agreement contribution'),
                                          ('developer-agreements', 'Developer agreement'),
                                          ('developer-agreement-transactions', 'Developer agreement transaction')])


class DeveloperAgreementForm(forms.Form):
    developer_agreement = forms.CharField(label='Developer agreement ID', max_length=20)
    developer_agreement_type = forms.ChoiceField(
        choices=[('section-106', 'Section 106'), ('community-infrastructure-levy', 'Community infrastructure levy')])
    organisation = forms.CharField(label='Local authority ID', max_length=20)
    entry_date = forms.DateField(label='The date this record is being created')
    start_date = forms.DateField(label='The date this agreement comes into effect')
    end_date = forms.DateField(label='The date this agreement is no longer in effect')
    planning_application = forms.CharField(label='Planning application ID', max_length=20)
    document_url = forms.CharField(label='The perminant URL where this document can be found', max_length=20)


class DeveloperAgreementContributionForm(forms.Form):
    developer_agreement_contribution = forms.CharField(label='Developer agreement contribution ID', max_length=20)
    developer_agreement = forms.CharField(label='Developer agreement ID', max_length=20)
    developer_contribution_purpose = forms.ChoiceField(choices=[
        ('affordable-housing', 'Affordable housing'),
        ('bonds', 'Bonds'),
        ('cil-administration-costs', 'CIL administration costs'),
        ('commumnity-facilities', 'Community facilities'),
        ('community-infrastructure-levy', 'Community infrastructure levy'),
        ('digital-infrastructure', 'Digital infrastructure'),
        ('economic-development', 'Economic development'),
        ('education', 'Education'),
        ('flood', 'Flood'),
        ('flood-and-water-management', 'Flood and water management'),
        ('green-infrastructure', 'Green infrastructure'),
        ('health', 'Health'),
        ('highways', 'Highways'),
        ('land', 'Land'),
        ('mayoral-community-infrastructure-levy', 'Mayoral Community Infrastructure Levy'),
        ('monitoring-fees', 'Monitoring fees'),
        ('neighbourhood-community-infrastructure-levy', 'Neighbourhood Community Infrastructure Levy'),
        ('open-space', 'Open space'),
        ('open-space-and-leisure', 'Open space and leisure'),
        ('other', 'Other'),
        ('transport', 'Transport'),
        ('transport-and-travel', 'Transport and travel'),
    ])
    amount = forms.FloatField(label='The contribution amount')
    entry_date = forms.DateField(label='The date this record is being created')
    start_date = forms.DateField(label='The date this agreement comes into effect')
    end_date = forms.DateField(label='The date this agreement is no longer in effect')


class DeveloperAgreementTransactionForm(forms.Form):
    developer_agreement_transaction = forms.CharField(label='Developer agreement transaction ID', max_length=20)
    developer_agreement_contribution = forms.CharField(label='Developer agreement contribution ID', max_length=20)
    amount = forms.FloatField(label='The transaction amount')
    entry_date = forms.DateField(label='The date this record is being created')
    start_date = forms.DateField(label='The date this agreement comes into effect')
    end_date = forms.DateField(label='The date this agreement is no longer in effect')


def dynamic_form():
   from wtforms import StringField
   from wtforms.fields.html5 import DateField
   from .schema import json
   from wtforms import Form

   fields = {'string': StringField, 'date': DateField}

   class DynamicForm(Form):

       def __init__(self):
           super().__init__()

   # schema_url = request.args.get('schema')
   # schema_json = requests.get(schema_url).json()
   schema_json = json

   for field in schema_json.get('fields'):
       field_type = fields.get(field.get('type'))
       if field_type is not None:
           # you can also pass validators into field_type constructor below based on constraints element
           f = field_type(field['title'])
           setattr(DynamicForm, field['title'].lower().replace(' ', '_'), f)
           print(f)

   return DynamicForm()
