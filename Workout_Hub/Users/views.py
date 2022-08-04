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

    
    try:
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
        #request.data["id"] = request.user.id
        new_trainee = TraineeSerializer(data=request.data)
        if new_trainee.is_valid():
            new_trainee.save()
            #TraineeGroup = Group.objects.get(name='TraineeGroup')
            #TraineeGroup.user_set.add(new_trainee)
        else:
            return Response({"msg" : "couldn't create a Trainee", "errors" : new_trainee.errors}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({"msg" : "Couldn't Create trainee", "error" : str(e) },status=status.HTTP_404_NOT_FOUND)


    return Response({"msg" : "Trainee created Successfully"}, status = status.HTTP_201_CREATED)


@api_view(['POST'])
def create_trainer(request : Request):

    try:
        new_user = UserSerializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
        #request.data["id"] = request.user.id
        new_trainer = TrainerSerializer(data=request.data)
        if new_trainer.is_valid():
            new_trainer.save()
            #TrainerGroup = Group.objects.get(name='TrainerGroup')
            #TrainerGroup.user_set.add(new_trainer)
        else:
            return Response({"msg" : "couldn't create a Trainer", "errors" : new_trainer.errors}, status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({"msg" : "Couldn't Create trainer", "error" : str(e) },status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "Trainer created Successfully"}, status = status.HTTP_201_CREATED)