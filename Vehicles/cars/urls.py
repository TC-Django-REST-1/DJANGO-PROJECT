from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_new_brand/', views.add_brand, name='add_new_brand'),
    path('brands_list/', views.brand_list, name='brand_list'),
    path('update_brand/<brand_id>', views.update_brand, name='update_brand'),
    path('remove_brand/<brand_id>', views.remove_brand, name='remove_brand'),


    path('brand_history/', views.brand_history_record, name='brand_history_record'),


    path('add_general_class/', views.add_general_class, name='add_general_class'),
    path('general_class_list/', views.general_class_list, name='general_class_list'),
    path('update_general_class/<general_class_id>', views.update_general_class, name='update_general_class'),
    path('remove_general_class/<general_class_id>', views.remove_general_class, name='remove_general_class'),


    # path('add_Brands_class/', views.add_Brands_class, name='add_Brands_class'),
    # path('Brands_class_list/', views.Brands_class_list, name='Brands_class_list'),
    # path('update_Brands_class/<Brand_class_id>', views.update_Brands_class, name='update_Brands_class'),
    # path('remove_Brands_class/<Brand_class_id>', views.remove_Brands_class, name='remove_Brands_class'),

    
    path('add_new_Category/', views.add_new_Category, name='add_new_Category'),
    path('Categories_list/', views.Categories_list, name='Categories_list'),
    path('update_category/<category_id>', views.update_category, name='update_category'),
    path('remove_category/<category_id>', views.remove_category, name='remove_category'),    
        
    
    # path('add_new_car/', views.add_car, name='add_new_car'),
    # path('cars_list/', views.cars_list, name='cars_list'),
    # path('update_car/<car_id>', views.update_car, name='update_car'),
    # path('remove_car/<car_id>', views.remove_car, name='remove_car'),


    # path('brand_cars/<brand_title>', views.brand_cars_list, name='brand_cars_list'),
]