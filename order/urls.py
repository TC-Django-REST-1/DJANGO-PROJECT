from django.urls import path
from . import views

name = "order"

urlpatterns = [
    path("add/", views.add_order, name="add_order"),
    path("delete/<int:order_id>", views.cancel_order, name="delete_order"),
    path("show/", views.show_orders, name="show orders"),
]