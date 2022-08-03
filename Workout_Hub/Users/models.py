from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Trainers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    tr_phone = models.IntegerField(blank=True)


class Trainees(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    te_phone = models.IntegerField(blank=True)
