from django.urls import path
from . import views

app_name = "stores"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<store_id>/", views.update, name="update"),
    path("delete/<store_id>/", views.delete, name="delete")
]
