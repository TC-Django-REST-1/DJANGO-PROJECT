from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_new_brand/', views.add_brand, name='add_new_brand'),
    path('brands_list/', views.brand_list, name='brand_list'),
    path('update_brand/<brand_id>', views.update_brand, name='update_brand'),
    path('remove_brand/<brand_id>', views.remove_brand, name='remove_brand'),

    path('brand_cars/<brand_title>', views.brand_cars_list, name='brand_cars_list'),
    
    path('add_new_car/', views.add_car, name='add_new_car'),
    path('cars_list/', views.cars_list, name='cars_list'),
    path('update_car/<car_id>', views.update_car, name='update_car'),
    path('remove_car/<car_id>', views.remove_car, name='remove_car'),
]