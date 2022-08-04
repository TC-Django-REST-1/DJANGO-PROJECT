from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization


class Team(models.Model):
    name = models.CharField(max_length=30, null=False, help_text="Name of the team")
    organization = models.ForeignKey(
        Organization,
        null=False,
        on_delete=models.CASCADE,
        help_text="Team organization",
        related_name="teams",
    )
    managers = models.ManyToManyField(
        User,
        help_text="Manager",
        related_name="teams_manager_in",
    )
    members = models.ManyToManyField(
        User, blank=True, help_text="Members", related_name="teams"
    )

    def __str__(self) -> str:
        return f"{self.name} ({self.organization.name})"
