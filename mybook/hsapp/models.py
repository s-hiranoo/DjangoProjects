from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.utils import timezone


class Dealer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    phone = models.IntegerField()
    name = models.CharField(max_length=128)
    state_id_number = models.CharField(max_length=128)
    state_id_picture = models.FileField(blank=True)
    birth_date = models.CharField(max_length=128)
    dependents = models.CharField(max_length=255)
    land_size = models.IntegerField(default=0)
    leased_land = models.BooleanField(default=False)
    previous_hs_client = models.BooleanField(default=False)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FieldOfficer(models.Model):
    name = models.CharField(max_length=255)
    farmers = models.ManyToManyField(Farmer, blank=True, default=[1])

    def __str__(self):
        return self.name


class VisitFarmer(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.CASCADE, default=1)
    done_or_appointment = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    check_in_time = models.TimeField(default=timezone.now)
    check_out_time = models.TimeField(default=timezone.now)


class VisitDealer(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, default=1)
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.CASCADE, default=1)
    done_or_appointment = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    check_in_time = models.TimeField(default=timezone.now)
    check_out_time = models.TimeField(default=timezone.now)

"""
class Visit(models.Model):
    customer_id = models.CharField(max_length=128)
    fo_id = models.CharField(max_length=128)
    done_or_appointment = models.BooleanField(default=False) # if done: False, appointment: True
    date = models.DateField(default=timezone.now)
    check_in_time = models.IntegerField()
    check_out_time = models.IntegerField()

    def __str__(self):
        return self.date
"""


class Plant(models.Model):
    name = models.CharField(max_length=128)
    species = models.CharField(max_length=128, blank=True)
    season_in = models.IntegerField()   # in month
    season_end = models.IntegerField()  # end month
    #season = models.CharField()      # summer, winter, etc

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, default=1)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=128)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProspectFarmer(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=128)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Escalation(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.CASCADE, default=1)
    tmo_call_required = models.BooleanField(default=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.date


class FarmerPlant(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, default=1)
    plant_period = models.DateField(default=timezone.now)
    major = models.BooleanField()  # If the farmer plants this crop as his main crop

    def __str__(self):
        return self.plant.name


class DealerFarmerRelation(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, default=1)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    close_relation = models.BooleanField(default=False)

    def __str__(self):
        return self.close_relation


class PurchaseHistory(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, default=1)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Plant, on_delete=models.CASCADE, default=1)
    date = models.DateField(default=timezone.now)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.date


class FarmerInterest(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, default=1)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, default=1)
    interested = models.BooleanField(default=False)
    quantity = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.plant.name


class DealerProduct(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    quantity = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.dealer.name

