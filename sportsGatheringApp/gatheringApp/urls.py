from django.urls import path
from . import views


app_name = 'gathering_app'

urlpatterns = [
path('all/', view=views.get_all_gathers, name='get_all_gathers'),
path('add/', view=views.add_gather, name='add_gather'),
path('update/<gather_id>', view=views.update_gather, name='Update_gather'),
path('delete/<gather_id>', view=views.delete_gather, name="delete_gather"),
path('join/<gather_id>', view=views.join_gather, name="join_gather"),
]