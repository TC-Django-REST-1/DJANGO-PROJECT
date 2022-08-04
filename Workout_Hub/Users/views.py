from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .seriallizers import TrainerSerializer, TraineeSerializer,UserSerializer
from rest_framework import status
from .models import Trainees, Trainers
from django.contrib.auth.models import Group

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.


@api_view(['POST'])
def signin(request : Request):

    username_from_client = request.data.get("username")
    password_from_client = request.data.get("password")

    user = authenticate(request, username=username_from_client, password=password_from_client)

    if user is None:
        return Response({"msg" : "user not found. Please check your credentials"}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg" : "You are authenticated successfully!", "token" : str(token)})


@api_view(['POST'])
def create_trainee(request : Request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        TrainerGroup = Group.objects.get(name='TrainerGroup')
        TrainerGroup.user_set.add(new_user)
    except Exception as e:
        return Response({"msg" : "Couldn't Create trainee", "error" : str(e)})

    phone = request.data["te_phone"]

    new_trainee = Trainees(user = new_user, te_phone = phone)
    new_trainee.save()

    return Response({"msg" : "Trainer created Successfully"}, status = status.HTTP_201_CREATED)

@api_view(['POST'])
def create_trainer(request : Request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        TraineeGroup = Group.objects.get(name='TraineeGroup')
        TraineeGroup.user_set.add(new_user)
    except Exception as e:
        return Response({"msg" : "Couldn't Create trainee", "error" : str(e)})

    phone = request.data["tr_phone"]

    new_trainer = Trainers(user = new_user, start_date = start_date, end_date = end_date, tr_phone = phone)
    new_trainer.save()

    return Response({"msg" : "Trainer created Successfully"}, status = status.HTTP_201_CREATED)
