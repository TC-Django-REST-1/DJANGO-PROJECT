from django.urls import path
from . import views

app_name = "organization" 

urlpatterns = [
    #Admin
    path("add/admin", views.new_admin, name="new_admin"),
    path("all/admins", views.read_admins, name="read_admins"),
    path("update/admin/<admin_id>", views.update_admin, name="update_admin"),
    path("delete/admin/<admin_id>", views.delete_admin, name="delete_admin"),
    #Services
    path("add/service", views.new_service, name="new_service"),
    path("all/services", views.read_service, name="read_service"),
    path("update/service/<service_id>", views.update_service, name="update_service"),
    path("delete/service/<service_id>", views.delete_service, name="delete_service"),
    path("search/<str:name>", views.search_service, name="search_service"),


    #Employees
    path("add/employee", views.new_employee, name="new_employee"),
    path("all/employees", views.read_employee, name="read_employee"),
    path("delete/employee/<employee_id>", views.delete_employee, name="delete_employee"),
    path("update/employee/<employee_id>", views.edit_employee, name="edit_employee"),

    

    #Companies
    path("add/company", views.new_company, name="new_company"),
    path("all/companies", views.read_companies, name="read_companies"),
    path("delete/company/<company_id>", views.delete_company, name="delete_company"),
    path("mycompany/",views.view_specific_companies,name="view_specific_companies"),
    path("update/company/<company_id>",views.edit_companies,name="edit_companies"),

    #Requests
    path("add/request", views.new_service_request, name="new_service_request"),
    path("myrequests/", views.view_specific_request, name="view_specific_request"),
    path("delete/request/<request_id>", views.delete_request, name="delete_request"),

    #task
    path("add/task", views.new_task, name="new_task"),
    path("delete/task/<task_id>", views.delete_task, name="delete_task"),

    

]