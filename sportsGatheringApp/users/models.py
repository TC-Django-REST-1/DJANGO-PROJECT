from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    isMale = models.BooleanField()
    phoneNumber = models.CharField(max_length=12)