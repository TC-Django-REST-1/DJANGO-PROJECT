from django.shortcuts import render 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.request import Request 
from rest_framework import status 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.tokens import AccessToken , Token

# Create your views here.


@api_view(['POST'])
def register_user(request: Request):

    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except Exception as e:
        return Response({"msg": "Couldn't create User", "error": e})

    return Response({"msg": "User created successfully"})



@api_view(['POST'])
def login_user (request: Request):
    client_username = request.data.get("username")
    client_password = request.data.get("password")
    
    user = authenticate(request, username=client_username, password=client_password)

    if user is None:
        return Response({"msg" : "user not found. Please check your credentials"}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg": "You're authenticated successfully", "token": str(token)})

