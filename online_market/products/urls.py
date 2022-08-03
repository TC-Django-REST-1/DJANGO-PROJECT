from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete")
]
