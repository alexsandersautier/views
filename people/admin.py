from django.contrib import admin
from . import models

class PersonModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birthdate', 'gender')
    search_fields = ('name', 'last_name', 'birthdate', 'gender')

admin.site.register(models.Person, PersonModelAdmin)