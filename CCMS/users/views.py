from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from uuid import uuid4

# Create your views here.
@api_view(['POST'])
def register_user(request : Request):

    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    id = uuid4

    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except Exception as e:
        return Response({"msg" : "Couldn't Create user", "error" : e})

    return Response({"msg" : "User Created Successfuly"}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def login_user(request : Request):

    username_from_client = request.data.get("username")
    password_from_client = request.data.get("password")

    user = authenticate(request, username=username_from_client, password=password_from_client)
  

    if user is None:
        return Response({"msg" : "Incorrect username or password"}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg" : "You are authenticated successfully!", "token" : str(token)})



# Get all users
@api_view(['GET'])
def read_users(request:Request):

    all_users = User.objects.all()
    list_of_users = [{"username":user.username,"email":user.email,"password":user.password} 
    for user in all_users]
    


    response_data = {
        "Message" : "All users List",
        "Users" : list_of_users
    }

    return Response(response_data,status=status.HTTP_200_OK)

    