from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", view=views.register_user, name="register_user"),
    path("login/", view=views.log_in, name="login"),
]