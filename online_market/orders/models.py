from django.db import models
from django.conf import settings

from products.models import Product

# Create your models here.


class Order(models.Model):
    address = models.TextField()
    date = models.DateField()
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')
