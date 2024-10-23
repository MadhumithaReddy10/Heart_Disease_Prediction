from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    dob = models.DateField(null=True, blank=True)


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phn_number = models.CharField(max_length=15)
    blood_pressure = models.CharField(max_length=10)
    sugar_levels = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)