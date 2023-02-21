from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default='')
    description = models.TextField(default='')
    image1 = models.ImageField(upload_to='images', default='')
    image2 = models.ImageField(upload_to='images', default='')
    image3 = models.ImageField(upload_to='images', default='')
    image4 = models.ImageField(upload_to='images', default='')

    def __str__(self):
        return self.name
