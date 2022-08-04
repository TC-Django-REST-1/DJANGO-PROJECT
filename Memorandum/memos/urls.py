from django.urls import path
from . import views 



urlpatterns = [
    # Categories ctgry
    path('ctgry/list/', views.list_category),
    path('ctgry/add/', views.create_category),
    path('ctgry/update/<cate_id>/', views.update_category),
    path('ctgry/del/<cate_id>/', views.del_category),


    # Tasks
    path('task/list/', views.list_task),
    path('task/add/', views.add_task),
    path('task/update/<task_id>/', views.update_task),
    path('task/del/<task_id>/', views.del_task),


    # Comments cmnt
    path('cmnt/list/', views.list_comment),
    path('cmnt/add/', views.add_comment),
    path('cmnt/update/<cmnt_id>/', views.update_comment),
    path('cmnt/del/<cmnt_id>/', views.del_comment),
]