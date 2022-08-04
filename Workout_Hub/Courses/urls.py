from django.urls import path
from . import views

app_name = "Courses"

urlpatterns = [
    path("courses/", views.view_courses, name="view_courses"),
    path("add/<trainer_id>/", views.add_course, name="add_course"),
    path("update/<course_id>/", views.course_update, name="course_update"),
    path("delete/<course_id>/", views.delete_course, name="delete_course"),
    path("register/<trainee_id>/", views.register_trainee, name="register_trainee")
]