from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('user_login/', views.user_login, name='user_login')
]