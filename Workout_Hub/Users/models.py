from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Trainers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #id = models.IntegerField(primary_key = True) 
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    tr_phone = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.user.username


class Trainees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key = True) 
    te_phone = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.user.username
