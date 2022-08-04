
from django.db import models
from django.contrib.auth.models import User
from category.models import Product
# Create your models here.

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_created=True)