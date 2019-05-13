from django.db import models

class LocalPlans(models.Model):
    name = models.CharField(max_length=40)
    organisation = models.CharField(max_length= 40)
    entrydate = models.DateField()
    state = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class DeveloperContributions(models.Model):
    developer_name= models.CharField(max_length=40)
    local_authoriy_name = models.CharField(max_length= 40)
    entry_date = models.DateField()
    the_lovely_things_we_will_get = models.CharField(max_length=40)

    def __str__(self):
        return self.name