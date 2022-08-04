from django.urls import path
from . import views

app_name = 'career_matching'

urlpatterns = [
    path('add_job/', views.add_job, name='add_job'),
    path('list_job/', views.list_job, name='list_job'),
    path('update_job/<job_id>/', views.update_job, name='update_job'),
    path('delete_job/<job_id>/', views.delete_job, name='delete_job'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('list_skill/', views.list_skill, name='list_skill'),
    path('update_skill/<skill_id>/', views.update_skill, name='update_skill'),
    path('add_jobs_skills_ids/', views.add_job_skill, name='delete_skill'),
    path('add_course/', views.add_course, name='add_course'),
    path('list_course/', views.list_course, name='list_course'),
    path('update_course/<course_id>/', views.update_course, name='update_course'),
    path('delete_course/<course_id>/', views.delete_course, name='delete_course'),
    path('list_courses_skills_of_job/', views.list_skills_courses_of_job, name='skills&courses for a job')
]