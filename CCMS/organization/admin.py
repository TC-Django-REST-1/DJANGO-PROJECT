from django.contrib import admin
from .models import Adminstration, Company, Service, Employee,Task,ManageRequset
# Register your models here.


class ManagerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','commercial_Id','mobile_number','address']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname','Birthdate','mobile_number','Department']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'service_duration','beneficiary_group','Fees']

# Register your models here.
admin.site.register(Adminstration, ManagerAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Service,ServiceAdmin)

