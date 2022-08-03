from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken

import re

email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

def email_validation(email):   
  
    if(re.search(email_pattern,email)):   
        return "Valid Email"
    else:   
        return None

# Create your views here.
@api_view(['POST'])
def register_user(request : Request):

    # username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    email_result = email_validation(email)
    print(email_result)

    if email_result == "Valid Email":
        username = email

    else:
        return Response({"msg" : "Couldn't Create a new user, e-mail is not valid "})
    

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
