from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    country = models.CharField(max_length=100, default="Saudi Arabia")
    region = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

## type choices
CHOICES = (
        ('1', 'historical'),
        ('2', 'religious'),
        ('3', 'entertainment'),
    )
class Place(models.Model):
    address = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=CHOICES)
    entry_fee = models.CharField(max_length=100, default="free")
    image_url = models.URLField(null=False)
    
    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self) -> str:
        return self.content