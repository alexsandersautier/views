from django.db import models
from util.constants import GENDERS

class Person(models.Model):
    id        = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    gender    = models.CharField(max_length=1, choices=GENDERS)
    photo = models.ImageField(upload_to='people/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'