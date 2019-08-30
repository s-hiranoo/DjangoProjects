from django.db import models


class Farmer(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    season = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FieldOfficer(models.Model):
    name = models.CharField(max_length=255)
    farmers = models.ManyToManyField(Farmer, blank=True)

    def __str__(self):
        return self.name
