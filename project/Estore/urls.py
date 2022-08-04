from django.urls import path
from . import views

app_name = "Estore"

urlpatterns = [
    #company
    path("add/", views.add_company, name="add_company"),
    path("update/<company_id>/", views.update_company, name="update_company"),
    path("delete/<company_id>/", views.delete_company, name="delete_company"),    
    #category
    path("category/add", views.add_category, name="add_category"),
    path("category/list", views.list_category, name="list_category"),   
    #product
    path('products/add/', views.add_product, name='add_product'),
    path('products/list/', views.list_product, name='list_product'),
    path("products/update/<update_product>/", views.update_product, name="update_product"),
    #comments
    path("comments/add/", views.add_comment, name="add_comment"),
    path("comments/all/", views.list_comments, name="list_all_comments"),
    path("comments/update/<comment_id>/", views.update_comment, name="update_book")
    
    ]
