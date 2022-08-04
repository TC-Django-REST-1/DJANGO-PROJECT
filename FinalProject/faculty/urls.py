from sys import implementation
from django.urls import URLPattern, path
from urllib.parse import urlparse
from . import views
from django.urls import path
app_name = "faculty"
URLPatterns = {

    path('facultyList/', views.dis, name="dis") 
}