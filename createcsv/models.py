from django.db import models
from django.forms import ModelForm

class LocalPlans(models.Model):
    name = models.CharField(max_length=40)
    organisation = models.CharField(max_length= 40)
    entrydate = models.DateField()
    state = models.CharField(max_length=40)

    def __str__(self):
        return self.name

# class CreateCsvForm(ModelForm):
#     class Meta:
#         model = LocalPlans
#         fields = ['name', 'organisation', 'entrydate', 'state']