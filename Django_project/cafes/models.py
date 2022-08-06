from tkinter import CASCADE
from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class Cafe(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    open_time=models.TimeField()
    close_time=models.TimeField()
    
    def __str__(self)->str:
        return self.name

class Product(models.Model):
    cafe = models.ForeignKey(Cafe,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description =  models.TextField()
    price =models.FloatField()

    def __str__(self) -> str:
        return self.name