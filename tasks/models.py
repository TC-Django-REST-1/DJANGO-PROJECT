from django.db import models
from organization.models import Organization
from teams.models import Team
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class TaskStatuses(models.TextChoices):
    Todo = _("Todo")
    InProgress = _("In progress")
    Completed = _("Completed")


class Task(models.Model):
    title = models.CharField(max_length=55, null=False, help_text="Task title")
    description = models.CharField(max_length=255, null=False, blank=True)
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, related_name="tasks"
    )
    team = models.ForeignKey(
        Team, null=True, on_delete=models.SET_NULL, related_name="tasks"
    )
    status = models.CharField(
        max_length=40,
        null=False,
        choices=TaskStatuses.choices,
        help_text="Task status",
    )
    assignees = models.ManyToManyField(
        User, blank=True, help_text="Assignees", related_name="tasks"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        help_text="Task creation date",
        editable=False,
    )
    completed_at = models.DateTimeField(
        default=None, null=True, blank=True, help_text="Task completion date"
    )

    def __str__(self) -> str:
        return f"{self.title} {self.status}"


class ReviewRequest(models.Model):
    author = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="review_requests"
    )
    task = models.ForeignKey(
        Task, null=False, on_delete=models.CASCADE, related_name="review_requests"
    )
    content = models.CharField(max_length=255, null=False, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=False,
    )


class Review(models.Model):
    author = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE, related_name="reviews"
    )
    task = models.ForeignKey(
        Task, null=False, on_delete=models.CASCADE, related_name="reviews"
    )
    request = models.ForeignKey(
        ReviewRequest,
        null=False,
        on_delete=models.CASCADE,
        related_name="reviews",
        help_text="The review request",
    )
    approved = models.BooleanField(
        default=False, help_text="Whether the review request was approved"
    )
    content = models.CharField(
        max_length=255, null=True, help_text="The content of the change request"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=False,
    )
