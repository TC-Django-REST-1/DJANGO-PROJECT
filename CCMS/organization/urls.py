from django.urls import path
from . import views

app_name = "organization" 

urlpatterns = [
    #Services
    path("add/service", views.new_service, name="new_service"),
    path("all/services", views.read_service, name="read_service"),
    path("update/service/<service_id>", views.update_service, name="update_service"),
    path("delete/service/<service_id>", views.delete_service, name="delete_service"),

    #Employees
    path("add/employee", views.new_employee, name="new_employee"),
    path("all/employees", views.read_employee, name="read_employee"),
    path("delete/employee/<employee_id>", views.delete_employee, name="delete_employee"),

    #Companies

    
]