from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("list/", views.users_list, name="users_list"),
    path('remove_user/<user_id>', views.remove_user, name='remove_user'),
    path('update_email/<user_id>', views.update_email, name='update_email'),
]