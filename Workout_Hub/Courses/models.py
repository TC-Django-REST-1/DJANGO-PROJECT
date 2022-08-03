from django.db import models
from Users.models import Trainer

# Create your models here.
class Courses(models.Model):
    c_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=218)
    c_type = models.CharField(max_length=218)
    c_duration = models.DecimalField()
    c_price = models.FloatField()