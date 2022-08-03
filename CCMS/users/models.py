from urllib import request
from django.db import models
# Create your models here.

class Cpmpany(models.Model):
    name = models.CharField(max_length=512)
    email = models.EmailField()
    password = models.CharField(max_length=512)
    commercial_Id = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=128)
    address = models.CharField(max_length=128)


class Consumer(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=128)

