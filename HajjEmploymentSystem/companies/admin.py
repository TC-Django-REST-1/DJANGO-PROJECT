from django.contrib import admin

from .models import Company, Job

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'permit_number', 'owner', 'category', 'no_of_pilgrims', 'location_url']
    # list_filter = ['name', 'owner']

class JobAdmin(admin.ModelAdmin):
    list_display = ['title','company','required_skills','salary','employee']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)