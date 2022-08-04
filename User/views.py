from django.db import IntegrityError

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken


# Create your views here.
User._meta.get_field('email')._unique = True


@api_view(['POST'])
def register_user(request: Request):

    
    try:
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.create_user(username, email, password)
        user.save()
        return Response({"msg": "User Created Successfuly"}, status=status.HTTP_201_CREATED)

    except IntegrityError:
        return Response({"msg": "Couldn't Create user the user already exists"},
                        status=status.HTTP_403_FORBIDDEN)
    except ValueError as e:
        return Response({"msg": e},status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def login_user(request: Request):

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(request, username=username,
                        password=password)

    if user is None:
        return Response({"msg": "user not found. Please check your credentials"}, status=status.HTTP_403_FORBIDDEN)

    token = AccessToken.for_user(user)

    return Response({"msg": "You are authenticated successfully!", "token": str(token)}, status=status.HTTP_202_ACCEPTED)
