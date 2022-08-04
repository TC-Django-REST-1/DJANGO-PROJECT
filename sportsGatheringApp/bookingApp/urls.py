from django import views
from django.urls import path
from . import views 



app_name = 'booking_app'

urlpatterns = [
path("all/", view=views.get_all_plaices, name="get_all_plaices"),
path("add/", view=views.add_place, name="add_place"),
path("update/<place_id>", view=views.update_place, name="update_place"),
path("delete/<place_id>", view=views.delete_place, name="delete_place"),
]