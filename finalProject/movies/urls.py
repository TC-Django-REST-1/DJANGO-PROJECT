
import imp
from django.urls import URLPattern, path 
from . import views

app_name = "movies"

urlpatterns = [
    # movies urls
    path("movie/add/", views.add_movie,name="add_movie"),
    path("movie/all/", views.list_movie,name="list_movie"),
    path("movie/moviebygenres/", views.list_movie_bygenres,name="list_movie"),
    path("movie/update/<movie_id>/", views.update_movie,name="update_movie"),
    path("movie/delete/<movie_id>/", views.delete_movie,name="delete_movie"),

    # schedule ulrs
    path("schedule/add/", views.add_schedule,name="add_schedule"),
    path("schedule/all/", views.list_schedule,name="list_schedule"),
    path("schedule/update/<schedule_id>/", views.update_schedule,name="update_schedule"),
    path("schedule/delete/<schedule_id>/", views.delete_schedule,name="delete_schedule"),

    # tickets urls
    path("ticket/add/", views.add_ticket,name="add_ticket"),
    path("ticket/all/", views.list_ticket,name="list_ticket"),
    path("ticket/update/<ticket_id>/", views.update_ticket,name="update_ticket"),
    path("ticket/delete/<ticket_id>/", views.delete_ticket,name="delete_ticket"),

    # feedback urls
    path("feedback/add/", views.add_feedback,name="add_feedback"),
    path("feedback/all/", views.list_feedback,name="list_feedback"),
]