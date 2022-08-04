from django.db import models
from django.conf import settings

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
