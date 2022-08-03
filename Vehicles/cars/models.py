from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    description = models.TextField()
    established_in = models.PositiveIntegerField()
    Origin = models.CharField(max_length=255)
    Founder = models.CharField(max_length=255)
    Headquarters = models.TextField()
    # Products_classes = models.ManyToManyField(ProductCategory, blank=True, null=True, blank=True, related)
    # Products_categories = models.ManyToManyField(ProductCategory, blank=True, null=True, blank=True, related)

class Classes(models.Model):
    pass

class Categories(models.Model):
    pass

    
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    clas = models.ForeignKey(Classes, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ongoing_product = models.BooleanField(default=False)



