from django.urls import path
from . import views

app_name = "localproduct"

urlpatterns = [
    path("add/", views.add_product, name="add_product"),
    path("all/", views.get_products, name="all_products"),
    path("update/<product_id>", views.update_product, name="update_product"),
    path("delete/<product_id>", views.delete_product, name="delete_product"),
]