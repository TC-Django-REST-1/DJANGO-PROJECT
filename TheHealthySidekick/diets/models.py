from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class diet(models.Model):
    diet_name = models.CharField(max_length=512)
    diet_desc = models.TextField()
    diet_details_url = models.URLField()
    coach = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.diet_name