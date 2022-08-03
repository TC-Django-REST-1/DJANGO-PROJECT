from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("signup/", views.create_account, name="create_account"),
    path("signin/", views.signin, name="signin"),
    path("register/", views.register_course, name="register_course")
]