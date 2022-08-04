from django.contrib import admin
from organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("supervisor", "name", "created_at")
    list_filter = (
        "supervisor",
        "employees",
    )


admin.site.register(Organization, admin_class=OrganizationAdmin)
