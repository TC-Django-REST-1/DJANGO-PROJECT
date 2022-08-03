from django.db import models
from Users.models import Trainers, Trainees

# Create your models here.
class Course(models.Model):
    c_trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    c_trainee = models.ManyToManyField(Trainees, blank=True)
    c_name = models.CharField(max_length=512)
    c_type = models.CharField(max_length=512)
    c_duration = models.DecimalField(max_digits=5, decimal_places=2)
    c_price = models.FloatField()