from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'c_trainer', 'c_type','c_duration','c_price']
    list_filter = ['c_trainer', 'c_trainee']

# Register your models here.
admin.site.register(Course, CourseAdmin)