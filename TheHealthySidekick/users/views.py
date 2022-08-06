import email
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.contrib.auth.models import User
from .serializers import UserTypeSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken 
from django.contrib.auth.models import Group

# Create your views here.

@api_view(["POST"])
def register(request : Request):
    
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    user_type = request.data.get("user_type")

    try:
        if user_type not in ["coach","trainee"]:
            return Response({"msg":"User must be of type (coach) or (trainee)."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username, email, password)
        user.save()

        if user_type == "coach":
            coachs = Group.objects.get(name='coachs') 
            coachs.user_set.add(user)
        
        if  user_type == "trainee":
            trainees = Group.objects.get(name='trainees') 
            trainees.user_set.add(user)

        ut_ser = UserTypeSerializer(data={"user":user.id, "user_type":request.data.get("user_type")})
        if ut_ser.is_valid():
            ut_ser.save()
        else:
            return Response({"msg" : "Couldn't save user type.", "errors" : UserTypeSerializer.errors}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"msg" : "User couldn't be created.", "error" : e})

    return Response({"msg":"User created successfully."}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request : Request):

    username_from_client = request.data.get("username")
    password_from_client = request.data.get("password")

    user = authenticate(request, username=username_from_client, password=password_from_client)

    if user is None:
        return Response({"msg" : "User not found. Please check your credentials."}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg" : "You have logged in successfully!", "token" : str(token)})