from . import views
from django.urls import path

app_name = "diets"

urlpatterns = [
    path("create/", views.create_diet, name="create_diet"),
    path("list/", views.list_diets, name="list_diets"),
    path("update/<int:diet_id>/", views.update_diet, name="update_diet"),
    path("delete/<int:diet_id>/", views.delete_diet, name="delete_diet")
]