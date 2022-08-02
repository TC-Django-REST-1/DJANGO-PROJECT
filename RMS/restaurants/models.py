from tkinter import CASCADE
from django.db import models


class Restaurants(models.Model):
    restaurant_name = models.CharField(max_length=270)
    city = models.CharField(max_length=120)
    estplaished_date = models.DateField()
    type_of_food = models.CharField(max_length=70)


class Meals(models.Model):
    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    meal_name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=3)
    calories = models.IntegerField()
    image_url = models.URLField()