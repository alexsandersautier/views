from django import forms
from . import models

class PersonModelForm(forms.ModelForm):

    class Meta:
        model  = models.Person
        fields = '__all__'