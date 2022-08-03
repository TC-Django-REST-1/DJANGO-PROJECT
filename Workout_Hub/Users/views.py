from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import TrainerSerializer, TraineeSerializer
from rest_framework import status
from .models import Trainee, Trainer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.

@api_view(['POST'])
def create_account(request : Request):

    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except Exception as e:
        return Response({"msg" : "Couldn't Create user", "error" : e})

    return Response({"msg" : "User Created Successfuly"}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def signin(request : Request):

    username_from_client = request.data.get("username")
    password_from_client = request.data.get("password")

    user = authenticate(request, username=username_from_client, password=password_from_client)

    if user is None:
        return Response({"msg" : "user not found. Please check your credentials"}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg" : "You are authenticated successfully!", "token" : str(token)})



@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def register_course(request : Request, course_id):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Users.register_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        request.data["course"] = course_id

    except Exception as e:
        return Response({"msg" : "Couldn't regiter the course", "error" : e})

    return Response({"msg" : "Course regitered Successfully"}, status = stat.HTTP_201_CREATED)