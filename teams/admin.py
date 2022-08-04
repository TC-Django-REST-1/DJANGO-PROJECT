from django.contrib import admin
from teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "organization",
    )
    list_filter = (
        "organization",
        "members",
        "managers",
    )


admin.site.register(Team, admin_class=TeamAdmin)
