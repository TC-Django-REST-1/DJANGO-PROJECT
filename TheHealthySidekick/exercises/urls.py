from . import views
from django.urls import path

app_name = "exercises"

urlpatterns = [
    path("create/", views.create_exercise, name="create_exercise"),
    path("list/", views.list_exercises, name="list_exercises"),
    path("update/<int:excer_id>/", views.update_exercise, name="update_exercise"),
    path("delete/<int:excer_id>/", views.delete_exercise, name="delete_exercise")
]