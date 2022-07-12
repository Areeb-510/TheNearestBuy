from django.contrib import admin
from .models import Shop
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')