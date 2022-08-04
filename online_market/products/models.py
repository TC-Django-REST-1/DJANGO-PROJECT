from stores.models import Store
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
