from django.db import models
from Courses.models import Courses
from django.contrib.auth.models import User


# Create your models here.
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    tr_phone = models.IntegerField()


class Trainee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Courses, on_delete=models.DO_NOTHING)
    te_phone = models.IntegerField()
