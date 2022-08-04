from django.db import models

# Create your models here.


class LocalMarket(models.Model):
    
    localmarketname = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    established_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=128)