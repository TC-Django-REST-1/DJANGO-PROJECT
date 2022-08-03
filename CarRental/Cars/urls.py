from django.urls import path
from . import views

app_name="Cars"


urlpatterns = [
    # Branch urls
    path('Branch/Create', views.create_Branch, name='create_branch'),
    path('Branch/list', views.list_Branchs, name='list_Branchs'),
    path('Branch/update/<branch_id>/', views.update_Branch, name='update_Branch'),
    path('Branch/delete/<branch_id>/', views.delete_Branch, name='delete_Branch'),

    # Car urls
    path('Car/Create', views.create_car, name='create_car'),
    path('Car/list', views.list_car, name='list_car'),
    path('Car/update/<car_id>/', views.update_car, name='update_car'),
    path('Car/delete/<car_id>/', views.delete_car, name='delete_car'),

    # reservedCar urls
    path('reservedCar/Create', views.create_reservedCar, name='create_reservedCar'),
    path('reservedCar/list', views.list_reservedCar, name='list_reservedCar'),
    path('reservedCar/update/<car_id>/', views.update_reservedCar, name='update_reservedCar'),
    path('reservedCar/delete/<car_id>/', views.delete_reservedCar, name='delete_reservedCar'),
]