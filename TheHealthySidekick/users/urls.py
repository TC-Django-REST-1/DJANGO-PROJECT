from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register_user"),
    path("login/", views.login, name="login_user")
]