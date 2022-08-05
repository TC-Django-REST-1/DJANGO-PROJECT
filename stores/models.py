from django.db import models

# Create your models here.

class Stores(models.Model):
  store_name = models.CharField(max_length=512)
  commercial_registration = models.IntegerField()
  store_description = models.TextField()

class Products(models.Model):
  stores = models.ForeignKey(Stores, on_delete=models.CASCADE)
  product_name = models.CharField(max_length=512)
  description = models.TextField()
  price = models.DecimalField(max_digits=6, decimal_places=2)
  image_url = models.URLField() 