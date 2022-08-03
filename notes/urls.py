from django.urls import path
from .views import add_note, list_notes, edit_note, delete_note

app_name = 'notes'

urlpatterns = [
    path('add/note/', add_note, name='add_note'),
    path('', list_notes, name='list_notes'),
    path('edit/note/<int:pk>/', edit_note, name='edit_note'),
    path('delete/note/<int:pk>/', delete_note, name='delete_note'),

]
