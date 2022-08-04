from django.db import models
from pkg_resources import require



# This model is to save all information about brand
class Brand(models.Model):
    brand = models.CharField(max_length=255)
    description = models.TextField()
    established_in = models.PositiveIntegerField()
    origin = models.CharField(max_length=255)
    founder = models.CharField(max_length=255)
    headquarters = models.TextField()
    last_revenue_billion = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.brand


# This model is to save all modifications that take place in any brand record,
#  answring these questions (when? who? did what?)
class BrandHistory(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=255)
    description = models.TextField()
    established_in = models.PositiveIntegerField()
    origin = models.CharField(max_length=255)
    founder = models.CharField(max_length=255)
    headquarters = models.TextField()
    last_revenue_billion = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.PositiveIntegerField()
    remarks = models.TextField(blank=True)
    modified_by = models.CharField(max_length=255)
    modification_date = models.DateField()

    def __str__(self):
        return self.brand

# # This model is to list the general classes that can be used to categorize any brand class 
# class GeneralClasses(models.Model):
#     general_class = models.CharField(max_length=255)

#     def __str__(self):
#         return self.general_class


# # This model is to save all information about classes in each brand like, Luxury cars ,Commercial cars, sport cars,
# class BrandsClasses(models.Model):
#     class_name = models.CharField(max_length=255)
#     class_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     general_class =  models.ForeignKey(GeneralClasses, on_delete=models.SET_DEFAULT, default='Need to be added manually')
#     targeted_customers = models.CharField(max_length=255)
#     quality = models.CharField(max_length=255)
#     exclusive = models.BooleanField(default=False)
#     remarks = models.TextField()

#     def __str__(self):
#         return self.class_name + " | " + self.class_brand.brand + " | " + self.general_class
    

# # This model is to save categories of all brands, Ex, sedan car, Family car, 4x4 car, Truks, industiral cars ... etc.
# class Categories(models.Model):
#     category_name = models.CharField(max_length=255)
#     targeted_customers = models.CharField(max_length=255)
#     targeted_cost_range = models.CharField(max_length=255)
#     Limited = models.BooleanField(default=False)
#     remarks = models.TextField()

    
# class Car(models.Model):
#     car_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     car_class = models.ForeignKey(BrandsClasses, on_delete=models.SET_DEFAULT, default='Need to be added manually')
#     category = models.ForeignKey(Categories, on_delete=models.SET_DEFAULT, default='Need to be added manually')
#     image_url = models.URLField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     ongoing_product = models.BooleanField(default=False)
