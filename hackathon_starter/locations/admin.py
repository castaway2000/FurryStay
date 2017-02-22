from django.contrib import admin
from .models import *


class LocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Location._meta.fields]

    class Meta:
        model=Location

admin.site.register(Location, LocationAdmin)