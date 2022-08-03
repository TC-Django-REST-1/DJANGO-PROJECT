from django.contrib import admin
from .models import Category, Task, Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class TaskAdmin(admin.ModelAdmin):
    list_filter = ['cate_id']

class CommentAdmin(admin.ModelAdmin):
    list_filter = ['task_id']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
