from django.db import models

# Create your models here.
class UserDetail(models.Model):
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    phonenumber = models.CharField(max_length=1000, unique=True)
    zipcode = models.CharField(max_length=500)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)
    minimumtransaction = models.DecimalField(max_digits=70, decimal_places=2)
    maximumtransaction = models.DecimalField(max_digits=70, decimal_places=2)
    emailaddress = models.EmailField()
    nameoncard = models.CharField(max_length=1000)
    cardnumber = models.CharField(max_length=100)
    expiryday = models.CharField(max_length=50)
    expirymonth = models.CharField(max_length=50)
    expiryyear = models.CharField(max_length=50)
    acctnumber = models.IntegerField(max_length=500)
    cardtype = models.CharField(max_length=500)
    cvv = models.IntegerField(max_length=5)

    def __str__(self):
        return self.nameoncard
