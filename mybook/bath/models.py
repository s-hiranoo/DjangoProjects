from django.db import models
from django.utils import timezone


class Member(models.Model):
    name = models.CharField(max_length=40, default='Nobody')
    done = models.BooleanField(default=False)
    reserve_time = models.IntegerField(default=20)

    def __str__(self):
        return self.name



