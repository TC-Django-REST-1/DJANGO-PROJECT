from django.urls import path
from .views import add_note, list_notes, edit_note, delete_note
from .views import add_comment, list_comments

app_name = 'notes'

urlpatterns = [
    path('add/note/', add_note, name='add_note'),
    path('', list_notes, name='list_notes'),
    path('edit/note/<int:pk>/', edit_note, name='edit_note'),
    path('delete/note/<int:pk>/', delete_note, name='delete_note'),
    path('add/comment/<int:pk>/', add_comment, name='add_comment'),
    path('comments/<int:pk>/', list_comments, name='list_comments'),
]
