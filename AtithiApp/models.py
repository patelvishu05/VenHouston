from django.db import models
from datetime import datetime

# Create your models here.
class Guest(models.Model):
    driverLicense = models.CharField(max_length=255)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    address1 = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    dob = models.DateField()
    checkin = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    checkout = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    adults = models.IntegerField(null=True)
    children = models.IntegerField(null=True)
    paymentAmount = models.IntegerField(null=True)
    petFee = models.IntegerField(default=0)
    roomNumber = models.IntegerField(null=True)
