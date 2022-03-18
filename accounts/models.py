from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)
    is_blocked =  models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=6)
    address_text = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    google_map_Link = models.CharField(max_length=200)

    def __str__(self):
    	return self.user.username





class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phonenumber = models.IntegerField()
    city = models.CharField(max_length=20)
    pincode = models.IntegerField()
    address_text = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    shope_name = models.CharField(max_length=100)
    risk_score = models.IntegerField()
    
    
    def __str__(self):
    	return self.user.username