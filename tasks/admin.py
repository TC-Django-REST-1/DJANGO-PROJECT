from django.contrib import admin
from tasks.models import Task, Review, ReviewRequest


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "organization",
        "team",
        "status",
        "created_at",
        "completed_at",
    )
    list_filter = ("organization", "status", "assignees", "team")

class ReviewRequestAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "task",
        "content",
        "created_at",
    )
    list_filter = (
        "author",
        "task",
    )

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "task",
        "request",
        "approved",
        "content",
        "created_at",
    )
    list_filter = (
        "author",
        "task",
        "request",
        "approved",
    )

admin.site.register(Task, admin_class=TaskAdmin)
admin.site.register(ReviewRequest, admin_class=ReviewRequestAdmin)
admin.site.register(Review, admin_class=ReviewAdmin)