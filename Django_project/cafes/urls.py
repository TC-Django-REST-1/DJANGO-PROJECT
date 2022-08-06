from django.urls import path
from . import views

app_name = "cafe"

urlpatterns = [
   
    path("add/", views.add_cafe, name="add_cafe"),
    path("list/", views.list_cafe, name="list_cafe"),
    path("list/<search>", views.list_cafe, name="list_cafe"),
    path("update/<cafe_id>/", views.update_cafe, name="update_cafe"),
    path("delete/<cafe_id>/", views.delete_cafe, name="delete_cafe"),
    path("product/delete/<product_id>/", views.delete_product, name="delete_product"),
    path("product/list/", views.list_product, name="list_product"),
    path("product/add/", views.add_product, name="add_product"),
    path("product/update/<product_id>/", views.update_product, name="update_product"),

        ]