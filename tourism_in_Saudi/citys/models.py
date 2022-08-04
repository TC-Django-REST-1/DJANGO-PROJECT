from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    country = models.CharField(max_length=100, default="Saudi Arabia")
    region = models.CharField(max_length=100)

## type choices
CHOICES = (
        ('1', 'historical'),
        ('2', 'religious'),
        ('3', 'entertainment'),
    )
class Place(models.Model):
    address = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, unique=True)
    type = models.CharField(max_length=100, choices=CHOICES)
    entry_fee = models.CharField(max_length=100, default="free")
    image_url = models.URLField(null=False)
    comments = models.TextField(null=True)