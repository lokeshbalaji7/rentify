from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    is_seller = models.BooleanField(default=False)

class Property(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.CharField(max_length=100)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    hospitals_nearby = models.BooleanField(default=False)
    colleges_nearby = models.BooleanField(default=False)