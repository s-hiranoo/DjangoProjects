from django.contrib import admin

from .models import Farmer, FieldOfficer, Dealer

admin.site.register(Dealer)
admin.site.register(Farmer)
admin.site.register(FieldOfficer)

"""
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'season', 'location')
    list_display_links = ('name', 'product', 'season', 'location')


admin.site.register(Farmer, FarmerAdmin)


class FieldOfficerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(FieldOfficer)


admin.site.register(Dealer)
"""