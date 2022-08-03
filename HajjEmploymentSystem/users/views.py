from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken


@api_view(['POST'])
def register_user(request : Request):

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
def login_user(request : Request):

    username_from_client = request.data.get("username")
    password_from_client = request.data.get("password")

    user = authenticate(request, username=username_from_client, password=password_from_client)

    if user is None:
        return Response({"msg" : "user not found. Please check your credentials"}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg" : "You are authenticated successfully!", "token" : str(token)})

@api_view(["GET"])
def all_users(request : Request):
    users = User.objects.all()

    all_users = [{"id" : user.id, "username" : user.username} for user in users]

    res_data = {
        "msg" : "A list of All Users",
        "books" : all_users
    }

    return Response(res_data, status=status.HTTP_200_OK)
