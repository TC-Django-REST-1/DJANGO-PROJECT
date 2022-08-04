from sys import implementation
from django.urls import URLPattern, path
from urllib.parse import urlparse
from . import views
from django.urls import path
app_name = "faculty"
URLPatterns = {

    path('facultyList/', views.dis, name="dis") ,
    path("add/", views.add_class, name="add_class"),
    path("update/<classid>/", views.update_class, name="update_class"),
    path("delete/<class_id>/", views.delete_class, name="delete_class"),

}
