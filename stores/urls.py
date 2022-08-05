from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
  path('add/store/', views.add_store, name="add_store"),
  path('list/stores/', views.list_stores, name="list_stores"),
  path('update/store/<store_id>/', views.update_store, name="update_store"),
  path('delete/store/<store_id>/', views.delete_store, name="delete_store"),

  path('add/product/',views.add_product, name="add_product"),
  path('list/products/',views.list_products, name="list_products"),
  path('update/product/<product_id>/',views.update_product, name="update_product"),
  path('delete/product/<product_id>/',views.delete_product, name="delete_product"),
]