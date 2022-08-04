from sys import implementation
from django.urls import URLPattern, path
from urllib.parse import urlparse
from . import views
from django.urls import path
app_name = "students_teachers"
URLPatterns = {

    path('list/', views.display, name="display") 
}