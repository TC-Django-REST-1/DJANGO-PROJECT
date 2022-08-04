from django.db import models
from users.models import UserInfo
from category.models import Product
# Create your models here.

class Order(models.Model):

    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    order = models.ForeignKey(Product, on_delete=models.CASCADE)