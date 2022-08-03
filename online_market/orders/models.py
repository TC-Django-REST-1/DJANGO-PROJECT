from products.models import Product
from customers.models import Customer
from django.db import models

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = [models.ForeignKey(Product, on_delete=models.CASCADE)]
    quantitiy = [models.IntegerField()]
    total = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
