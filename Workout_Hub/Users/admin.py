from django.contrib import admin

from .models import Trainers, Trainees

class TrainerAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date','tr_phone']


class TraineeAdmin(admin.ModelAdmin):
    list_display = ['user', 'te_phone']

# Register your models here.
admin.site.register(Trainers, TrainerAdmin)
admin.site.register(Trainees, TraineeAdmin)