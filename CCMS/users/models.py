from django.db import models
# Create your models here.

class Consumer(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=128)

