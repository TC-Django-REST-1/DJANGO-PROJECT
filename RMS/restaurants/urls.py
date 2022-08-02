from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_restaurant, name="add_restaurant"),
    path('display/',views.list_restaurants, name="list_restaurants"),
    path('update/<restaurant_id>/',views.update_restaurant, name="update_restaurant"),
    path('delete/<restaurant_id>/',views.delete_restaurant, name="delete_restaurant"),
    
    path('add_meal/',views.add_meal, name="add_meal"),
    path('display_meals/',views.list_meals, name="list_meals"),
    path('update_meal/<meal_id>/',views.update_meal, name="update_meal"),
    path('delete_meal/<meal_id>/',views.delete_meal, name="delete_meal"),
]

