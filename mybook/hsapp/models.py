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
    state_id_picture = models.FileField()
    birth_date = models.CharField(max_length=128)
    dependents = models.CharField(max_length=255)
    land_size = models.IntegerField()
    leased_land = models.BooleanField()
    previous_hs_client = models.BooleanField(default=False)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FieldOfficer(models.Model):
    name = models.CharField(max_length=255)
    farmer_ids = models.CharField(max_length=255, validators=[validate_comma_separated_integer_list])

    def __str__(self):
        return self.name


class Visit(models.Model):
    customer_id = models.CharField(max_length=128)
    fo_id = models.CharField(max_length=128)
    done_or_appointment = models.BooleanField(default=False) # if done: False, appointment: True
    date = models.DateField(default=timezone.now)
    check_in_time = models.IntegerField()
    check_out_time = models.IntegerField()

    def __str__(self):
        return self.date


class Plant(models.Model):
    name = models.CharField(max_length=128)
    species = models.CharField(max_length=128)
    season_in = models.IntegerField()   # in month
    season_end = models.IntegerField()  # end month
    season = models.IntegerField()      # summer, winter, etc

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    plant_id = models.IntegerField()
    company_id = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class ProspectFarmer(models.Model):
    name = models.CharField(max_length=128)
    farmer_id = models.IntegerField() # ID of farmer who introduced him to fo
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class Escalation(models.Model):
    fo_id = models.IntegerField()
    farmer_id = models.IntegerField()
    tmo_call_required = models.BooleanField(default=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.date


class FarmerPlant(models.Model):
    plant_id = models.IntegerField()
    farmer_id = models.IntegerField()
    plant_period = models.DateField()
    major = models.BooleanField()  # If the farmer plants this crop as his main crop

    def __str__(self):
        return self.plant_id


class DealerFarmerRelation(models.Model):
    dealer_id = models.IntegerField()
    farmer_id = models.IntegerField()
    close_relation = models.BooleanField()

    def __str__(self):
        return self.dealer_id


class PurchaseHistory(models.Model):
    farmer_id = models.IntegerField()
    dealer_id = models.IntegerField()
    plant_id = models.IntegerField()
    product_id = models.IntegerField()
    date = models.DateField(default=timezone.now)
    price = models.IntegerField()

    def __str__(self):
        return self.date


class FarmerInterests(models.Model):
    farmer_id = models.IntegerField()
    plant_id = models.IntegerField()
    product_id = models.IntegerField()
    interested = models.BooleanField()
    quantity = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.plant_id


class DealerProducts(models.Model):
    dealer_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.dealer_id

