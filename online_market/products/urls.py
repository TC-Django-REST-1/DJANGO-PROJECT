from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("create/<store_id>/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<product_id>/", views.update, name="update"),
    path("delete/<product_id>/", views.delete, name="delete")
]
