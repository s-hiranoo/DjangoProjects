from django.contrib import admin

from .models import *

admin.site.register(Dealer)
admin.site.register(Farmer)
admin.site.register(FieldOfficer)
admin.site.register(VisitFarmer)
admin.site.register(VisitDealer)
admin.site.register(Plant)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(ProspectFarmer)
admin.site.register(Escalation)
admin.site.register(FarmerPlant)
admin.site.register(FarmerInterest)
admin.site.register(DealerFarmerRelation)
admin.site.register(PurchaseHistory)
admin.site.register(DealerProduct)



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