from django.urls import path
from . import views

app_name = "Users"

urlpatterns = [
    path("trainer/", views.create_trainer, name="create_trainer"),
    path("trainee/", views.create_trainee, name="create_trainee"),
    path("signin/", views.signin, name="signin"),
]