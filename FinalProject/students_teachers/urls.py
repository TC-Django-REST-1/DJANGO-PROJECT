from sys import implementation
from django.urls import URLPattern, path
from urllib.parse import urlparse
from . import views
from django.urls import path
app_name = "students_teachers"
URLPatterns = {

    path('list/', views.display, name="display") ,
    path("add/", views.add_student, name="add_student"),
    path("update/<student_id>/", views.update_student, name="update_student"),
    path("delete/<student_id>/", views.delete_student, name="delete_student"),
}