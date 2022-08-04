from django.urls import path
from . import views

name = "category"

urlpatterns = [
    path("add/", views.add_brand, name="add_brand"),
    path("all/", views.show_brand, name="show_brands"),
    path("update/<int:brand_id>", views.update_brand, name="update brand"),
    path("delete/<int:brand_id>", views.delete_brand, name="delete_brand"),
    path("product/add/", views.add_product, name="add_product"),
    path("product/all/", views.show_products, name="show_products"),
    

]