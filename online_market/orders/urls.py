from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<order_id>/", views.update, name="update"),
    path("delete/<order_id>/", views.delete, name="delete"),
    path("create_order_product/",
         views.create_order_product, name="create_order_product"),
    path("read_order_product/",
         views.read_order_product, name="read_order_product"),
    path("update_order_product/<order_product_id>/",
         views.update_order_product, name="update_order_product"),
    path("delete_order_product/<order_product_id>/",
         views.delete_order_product, name="delete_order_product")
]
