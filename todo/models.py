from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="todos",
        help_text="Author of the todo",
    )
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=355)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
