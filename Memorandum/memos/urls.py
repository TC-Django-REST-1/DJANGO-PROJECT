from django.urls import path
from . import views 



urlpatterns = [
    # Categories ctgry
    path('listctgry/', views.list_category),
    path('addctgry/', views.create_category),
    path('updatectgry/', views.update_category),
    path('delctgry/', views.del_category),


    # Tasks
    path('listtask/', views.list_task),
    path('addtask/', views.add_task),
    path('updatetask/', views.update_task),
    path('deltask/', views.del_task),


    # Comments cmnt
    path('listcmnt/', views.list_comment),
    path('addcmnt/', views.add_comment),
    path('updatecmnt/', views.update_comment),
    path('delcmnt/', views.del_comment),
]