from django.urls import path
from .views import TodoView, TodosView

urlpatterns = [
    path("", TodosView.as_view(), name="todos"),
    path("<pk>/", TodoView.as_view(), name="todo"),
]
