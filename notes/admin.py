from django.contrib import admin
from .models import Note, Comment

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'updated')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('note', 'user', 'comment', 'created', 'updated')