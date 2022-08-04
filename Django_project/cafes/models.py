from tkinter import CASCADE
from django.db import models

# Create your models here.

class Cafe(models.Model):
    name=models.CharField(max_length=200)
    products_num =models.IntegerField()
    established_at=models.DateField()
    city=models.CharField(max_length=200)

    def __str__(self)->str:
        return self.name 


class Product(models.Model):
    cafe = models.ForeignKey(Cafe,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description =  models.TextField()
    image_url = models.URLField()
    price =models.FloatField()

    def __str__(self) -> str:
        return self.name