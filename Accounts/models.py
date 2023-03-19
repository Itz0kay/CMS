from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=200, unique=True, blank=False)
    password = models.CharField(max_length=200, blank=False)
    firstname = models.CharField(max_length=200, blank=False)
    lastname = models.CharField(max_length=200, blank=False)

    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=200) 
    state = models.CharField(max_length=200) 
    country = models.CharField(max_length=200) 
    pincode = models.CharField(max_length=6, blank=False)

