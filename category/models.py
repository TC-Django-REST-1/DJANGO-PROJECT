from django.db import models

# Create your models here.

class Brand(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)


class Product(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    quantity = models.IntegerField(default=0)


