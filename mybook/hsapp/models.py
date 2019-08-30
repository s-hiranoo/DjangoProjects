from django.db import models


class Dealer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    season = models.IntegerField()
    location = models.CharField(max_length=255)
    dealers = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FieldOfficer(models.Model):
    name = models.CharField(max_length=255)
    farmers = models.ManyToManyField(Farmer, blank=True)

    def __str__(self):
        return self.name

