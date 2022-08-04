from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("list/", views.users_list, name="users_list"),
    path("update_password/<user_id>", views.update_password, name="update_user_password"),
    
]