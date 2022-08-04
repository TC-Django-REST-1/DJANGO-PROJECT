from api.serializers import UserSerializer, UserDataSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User


@api_view(["POST"])
def register(request: Request) -> Response:
    """
    Register a new user, expiration date of token is 1 hour, and expiration date of refresh token is 1 day.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.create(request.data)
            return Response(
                {
                    "msg": f"'{serializer.data.get('username')}' created successfully",
                },
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as err:
            return Response(
                {"code": "ValidationError", "errors": err},
                status=status.HTTP_400_BAD_REQUEST,
            )
    return Response(
        {"msg": "Bad request", "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )


class ListUsers(ListAPIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated, IsAdminUser,]
    serializer_class = UserDataSerializer
    queryset = User.objects.all()
