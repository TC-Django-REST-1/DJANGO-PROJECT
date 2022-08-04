from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken

from .models import userInfo 
from .serializers import userInfoSerializer
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def register_user(request : Request):
    data = request.data
    
    userName = data.get('userName')
    email = data.get('email')
    password = data.get('password')

    try:
        newUser = User.objects.create_user(userName,email,password)
        newUser.save()
    except Exception as e:
        return Response({"msg": "Sorry couldn't register a User!", "error":e},status=status.HTTP_403_FORBIDDEN)
    
    newUserInfo = userInfo(
        user=newUser ,name=data.get('name'),age=data.get('age'),isMale=data.get('isMale') ,phoneNumber=data.get('phoneNumber')
        )
    
    newUserInfo.save()

    return Response({"msg": "The user registered Successfully!"},status=status.HTTP_201_CREATED)



@api_view(["POST"])
def log_in(request : Request):

    data = request.data

    clint_UserName = data.get("userName")
    clint_password = data.get("password")

    user = authenticate(request=request, username=clint_UserName, password=clint_password)

    if user is None:
        return Response({"msg": "user not found. Please check your credentials"},status=status.HTTP_403_FORBIDDEN)

    token = AccessToken.for_user(user)

    return Response({"msg": "You are authenticated successfully!", "token": str(token)},status=status.HTTP_200_OK)


    