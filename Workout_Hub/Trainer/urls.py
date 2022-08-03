from django.urls import path
from . import views

app_name = "Trainer"

urlpatterns = [
    path("register/", views.create_account, name="create_account"),
    path("login/", views.login, name="login"),
    path("courses/", views.view_courses, name="view_courses"),
    path("add/", views.add_course, name="add_course"),
    path("update/", views.update_course, name="update_course")
]