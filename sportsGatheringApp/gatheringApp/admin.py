from django.contrib import admin
from .models import gather, GatherPlayers



class GatherAdmin(admin.ModelAdmin):
    list_display = [
        'sport',
        'maxLimit',
        'currentPlayers',
        'justFemales',
        'matchDateTime',
        'cost',
        'city',
        'location',
        'leader',
        'leaderPhoneNumber',
          ]

# class GatherPlayersAdmin(admin.ModelAdmin):
#     list_display = ['players','gather']

# Register your models here.
admin.site.register(gather, GatherAdmin)
admin.site.register(GatherPlayers)