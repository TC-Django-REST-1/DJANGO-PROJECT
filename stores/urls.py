from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
  path('add_store/', views.add_store, name="add_store"),
  path('list_stores/', views.list_stores, name="list_stores"),
  path('update_store/<store_id>/', views.update_store, name="update_store"),
  path('delete_store/<store_id>/', views.delete_store, name="delete_store"),

  path('add_product/',views.add_product, name="add_product"),
  path('list_products/',views.list_products, name="list_products"),
  path('update_product/<product_id>/',views.update_product, name="update_product"),
  path('delete_product/<product_id>/',views.delete_product, name="delete_product"),
]