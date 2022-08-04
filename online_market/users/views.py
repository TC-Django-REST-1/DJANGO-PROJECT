from .serializers import UserSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken

# Create your views here.


@api_view(['POST'])
def create(request: Request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
    else:
        return Response(
            {
                "msg": "Error, couldn't create user.",
                "error": user_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "User created."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
def login(request: Request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response(
            {
                "msg": "Missing credential."
            },
            status=status.HTTP_403_FORBIDDEN
        )

    user = authenticate(username=username, password=password)
    if user is None:
        return Response(
            {
                "msg": "User not found, check credential."
            },
            status=status.HTTP_403_FORBIDDEN
        )
    token = AccessToken.for_user(user)

    return Response(
        {
            "msg": "User authenticated.",
            "token": str(token)
        },
        status=status.HTTP_201_CREATED
    )
