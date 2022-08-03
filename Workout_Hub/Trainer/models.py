from django.db import models

# Create your models here.
class Trainer(models.Model):
    tr_name = models.CharField(max_length=218)
    start_date = models.DateField()
    end_date = models.DateField()
    tr_phone = models.IntegerField()
    tr_email = models.EmailField()
    tr_password = models.TextField()


class Course(models.Model):
    c_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=218)
    c_type = models.CharField(max_length=218)
    c_duration = models.DecimalField()
    c_price = models.FloatField()
