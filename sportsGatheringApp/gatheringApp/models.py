from django.db import models
from django.contrib.auth.models import User

from users.models import userInfo

# Create your models here.


class gather(models.Model):
    sport = models.CharField(max_length=128)
    maxLimit = models.IntegerField()
    currentPlayers = models.IntegerField()
    justFemales = models.BooleanField()
    matchDateTime = models.DateTimeField()
    cost = models.DecimalField(max_digits=6,decimal_places=2)
    city = models.CharField(max_length=128)
    location = models.URLField()
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    leaderPhoneNumber = models.CharField(max_length=12)



class GatherPlayers(models.Model):
    players = models.ManyToManyField(userInfo)
    gather = models.OneToOneField(gather, on_delete=models.CASCADE)