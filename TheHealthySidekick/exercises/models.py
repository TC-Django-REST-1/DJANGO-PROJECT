from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class exercise(models.Model):
    exercise_name = models.CharField(max_length=512)
    exercise_desc =  models.TextField()
    exercise_reps = models.IntegerField()
    exercise_sets = models.IntegerField()
    exercise_vid = models.URLField()
    exercise_intensity = models.CharField(max_length=512)
    coach = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.exercise_name
    

 