from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Organization(models.Model):
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="own_organizations"
    )
    name = models.CharField(
        max_length=60,
        null=False,
        validators=[
            MinLengthValidator(
                3, message="The minimum length of the organization name is 3"
            )
        ],
    )
    employees = models.ManyToManyField(User, blank=True, related_name="organizations")
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        editable=False,
    )

    def __str__(self) -> str:
        return f"{self.name}"
