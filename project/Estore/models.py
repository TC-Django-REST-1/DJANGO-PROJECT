from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='products')
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')


    def __str__(self) -> str:
        return self.content

    # book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


