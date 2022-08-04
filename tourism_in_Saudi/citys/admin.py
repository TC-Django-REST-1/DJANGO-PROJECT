from django.contrib import admin

from .models import City, Place, Comment
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'region']


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'type']
    list_filter = ['address', 'type']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['place', 'user', 'content']
    list_filter = ['place']

admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Comment, CommentAdmin)