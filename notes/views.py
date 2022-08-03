import imp
from unicodedata import name
from django.shortcuts import render, get_object_or_404
# rest framework
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication
# user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# models
from .models import Note, Comment
from .serializers import NoteSerializer, Commenterializer

# require auth for add notes views
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_note(request: Request):
    user = request.user
    if not user.is_authenticated:
        return Response({
            'msg': 'Please login!'
        }, status=HTTP_401_UNAUTHORIZED)
    if not user.has_perm('notes.add_note'):
        return Response({
            'msg': 'You do not have permission to add notes'
        }, status=HTTP_403_FORBIDDEN)

    request.data['user'] = user.id
    note = NoteSerializer(data=request.data)
    if note.is_valid():
        note.save()
    else:
        Response({
            'msg': 'Note not created',
            'error': note.errors
        }, status=HTTP_201_CREATED)

    return Response({
        'msg': f'Note {note.data.get("name")} created successfully',
    }, status=HTTP_201_CREATED)


# list all notes
@api_view(['GET'])
def list_notes(request: Request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)   
    return Response(serializer.data)

# edit note
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def edit_note(request: Request, pk: int):
    user = request.user
    if not user.is_authenticated:
        return Response({
            'msg': 'Please login!'
        }, status=HTTP_401_UNAUTHORIZED)
    if not user.has_perm('notes.change_note'):
        return Response({
            'msg': 'You do not have permission to edit notes'
        }, status=HTTP_403_FORBIDDEN)

    note = get_object_or_404(Note, pk=pk)
    if note.user != user:
        return Response({
            'msg': 'You do not have permission to edit this note'
        }, status=HTTP_403_FORBIDDEN)

    request.data['user'] = user.id
    serializer = NoteSerializer(note, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'msg': f'Note {note.name} updated successfully'
        }, status=HTTP_201_CREATED)
    else:
        return Response({
            'msg': 'Note not updated',
            'error': serializer.errors
        }, status=HTTP_201_CREATED)

# delete note
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_note(request: Request, pk: int):
    user = request.user
    if not user.is_authenticated:
        return Response({
            'msg': 'Please login!'
        }, status=HTTP_401_UNAUTHORIZED)
    if not user.has_perm('notes.delete_note'):
        return Response({
            'msg': 'You do not have permission to delete notes'
        }, status=HTTP_403_FORBIDDEN)

    note = get_object_or_404(Note, pk=pk)
    if note.user != user:
        return Response({
            'msg': 'You do not have permission to delete this note'
        }, status=HTTP_403_FORBIDDEN)

    note.delete()
    return Response({
        'msg': f'Note {note.name} deleted successfully'
    }, status=HTTP_201_CREATED)