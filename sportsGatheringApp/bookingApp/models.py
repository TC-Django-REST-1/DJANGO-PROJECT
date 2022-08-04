from django.db import models

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=128)
    contactInfo = models.CharField(max_length=12)
    bookedAt = models.DateField(default="2000-1-1")