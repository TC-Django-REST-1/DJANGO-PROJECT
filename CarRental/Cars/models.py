from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Branch Model
class Branch(models.Model):
    name=models.CharField(max_length=512)
    city=models.CharField(max_length=512)
    location= models.CharField(max_length=512)

# Car Model
class Car(models.Model):
    name=models.CharField(max_length=512)
    type=models.CharField(max_length=512)
    description = models.TextField()
    image_url= models.URLField()
    price= models.FloatField()
    is_available=models.BooleanField()
    branch=models.ForeignKey(Branch, on_delete=models.CASCADE)

# Car Reserved Model
class reservedCar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    car=models.ForeignKey(Car, on_delete=models.CASCADE)
    startDate=models.DateField()
    endDate=models.DateField()
    is_vaild= models.BooleanField() 