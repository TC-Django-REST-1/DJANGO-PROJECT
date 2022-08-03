from django.urls import path

from . import views

app_name = "companies"

urlpatterns = [
    path("add/", views.add_company, name="add_company"),
    path("all/", views.list_companies, name="list_companies"),
    path("update/<company_id>/", views.update_company, name="update_company"),
    path("delete/<company_id>/", views.delete_company, name="delete_company"),
    #jobs
    path("jobs/add/", views.add_job, name="add_job"),
    path("jobs/all/", views.list_jobs, name="list_jobs"),
    path("jobs/update/<job_id>/", views.update_job, name="update_job"),
    path("jobs/delete/<job_id>/", views.delete_job, name="delete_job"),
    path("jobs/apply/<job_id>/", views.apply_to_job, name="apply_to_job"),
    path("jobs/appointing_employee/<job_id>/<applicant_id>/", views.appointing_employee, name="appointing_employee")
]