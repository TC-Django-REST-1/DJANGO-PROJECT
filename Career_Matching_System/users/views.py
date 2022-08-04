from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

# ----------------------------- Create User ---------------------- #

@api_view(['POST'])
def add_user(request: Request):
    
    username = request.data['username']
    password = request.data['password']


    try:
        user = User.objects.create_user(username, password)
        user.save()
    except Exception as e:
        return Response({'message' : 'Could not create user', 'Error' : e})

    return Response({'message' : 'user created successfully!'}, status=status.HTTP_201_CREATED)


# ----------------------------- User Login -------------------------------- #

@api_view(['POST'])
def user_login(request: Request):
    
    user_name = request.data['username']
    passwd = request.data['password']

    user = authenticate(request, username=user_name,  password=passwd)

    if user is None:
        return Response({'message' : 'user not authenticated. Please check your credentials again!'}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({'message' : 'You are authenticated!', 'Token' : str(token)})

