from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Hospital


@admin.register(Hospital)
class HospitalAmdin(LeafletGeoAdmin):
    list_display = ["name", "la", "lo", "beds", "province_name"]
