from django.shortcuts import render
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def register_user(request : Request):
  username = request.data.get("username")
  email = request.data.get("email")
  password = request.data.get("password")
  try:
    user = User.objects.create_user(username, email, password)
    user.save()
  except Exception as e:
    return Response({"msg" : "Something went wrong :|", "err" : e})
  return Response({"msg" : "User created successfuly"}, status=201)

@api_view(['POST'])
def login_user(request : Request):
  user = authenticate(request, username=request.data.get("username"), password=request.data.get("password"))
  if user is None:
    return Response({"msg" : "User not found!"}, status=403)
  token = AccessToken.for_user(user)
  return Response({"msg" : "User logged in successfully!", "token" : str(token)})