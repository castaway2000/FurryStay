from django.contrib import admin
from .models import *


class LocationVisitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in LocationVisit._meta.fields]

    class Meta:
        model=LocationVisit

admin.site.register(LocationVisit, LocationVisitAdmin)