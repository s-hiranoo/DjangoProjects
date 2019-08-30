from django.contrib import admin

from .models import Farmer, FieldOfficer


class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'season', 'location')
    list_display_links = ('name', 'product', 'season', 'location')


admin.site.register(Farmer, FarmerAdmin)


class FieldOfficerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(FieldOfficer)
