from django.urls import path
from . import views 

app_name = "citys"

urlpatterns = [
    path("add/", views.add_city, name="add_city"),
    path("all/", views.list_city, name="list_all_citys"),
    path("update/<city_id>/", views.update_city, name="update_city"),
    path("delete/<city_id>/", views.delete_city, name="delete_city"),
    ## places
    path("places/add/", views.add_place, name="add_place"),
    path("places/all/", views.list_place, name="list_all_places"),
    path("places/update/<place_id>/", views.update_place, name="update_place"),
    path("places/delete/<place_id>/", views.delete_place, name="delete_place"),
    ## Comments
    path("places/comments/all/", views.list_comments, name="list_all_comments"),
    path("places/comments/add/", views.add_comment, name="add_comment"),
    path("places/comments/delete/<comment_id>/", views.delete_comment, name="delete_comment")
]