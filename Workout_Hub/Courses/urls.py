from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("courses/", views.view_courses, name="view_courses"),
    path("add/", views.add_course, name="add_course"),
    path("update/", views.update_course, name="update_course"),
    path("delete/", views.delete_course, name="delete_course")
]