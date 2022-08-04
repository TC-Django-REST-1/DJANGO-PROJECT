from django.contrib import admin
from .models import Job, Skill, Course, Skill_Job

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'Address']

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name' , 'type']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(Job, JobAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Course, CourseAdmin)