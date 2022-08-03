from email.policy import default
from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

app_lable = "store_model"

typeOfProdect = (
    ('Food', 'Food'),
    ('Juice', 'Juice'),
    ('Snack', 'Snack'))


class Brand(models.Model):
    brand_name = models.CharField(max_length=512, primary_key=True)
    established_at_Year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.now().year)],
        help_text="Use the following format: <YYYY>")

    def __str__(self) -> str:
        return self.brand_name

    def to_dict(self):
        return {"brand_name": self.brand_name, "established_at_Year": self.established_at_Year}

    class meta:
        ordering = ['brand']


class Product(models.Model):

    brand: Brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=typeOfProdect)
    add_at = models.CharField(max_length=50, auto_created=True,
                              default=datetime.now().strftime("%d/%m/%Y at %I:%M%p"), editable=False)
    description = models.TextField(
        blank=True,  default="no cooment", null=True,)
    image_url = models.URLField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self) -> str:
        brand = self.brand.objects.all()
        print(brand)
        return f"ID : {self.id} Berand:{brand} Name: {self.product_name}"

    class meta:
        app_label = 'Product'
        # ordering = ['product_name']
