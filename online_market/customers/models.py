from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=512)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=512)
    address = models.TextField()
    created_at = models.DateField()
