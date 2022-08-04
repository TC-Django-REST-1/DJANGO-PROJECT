from ast import mod
from django.db import models
from localmarket.models import localmarket
# Create your models here.

class LocalProduct(models.Model):

    localmarket = models.ForeignKey(localmarket, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

