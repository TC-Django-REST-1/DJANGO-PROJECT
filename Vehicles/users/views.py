from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .serializers import UserSerilizer,UserpasswordSerilizer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken

import re
import hashlib

# User._meta.get_field('email')._unique = True

def hasher(password):
    """ This function is to calculate the hash based on sha256 algorithm by passing the 'password' from the user and save
    it as hash """

    hasher = hashlib.sha256()  # To initialize a variable that uses sha256 algorithm for hashing
    hasher.update(password)  # Add the new part to the hasher for applying the sha256 on it
    output = hasher.hexdigest()  # Is the method to give the hashing result in hexadecimal type
    return output  # Return the result as hexadecimal code



email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

def email_validation(email):
    '''This function is to validate the email that enterd by a new user using  Regular Expressions method'''  
    if(re.search(email_pattern,email)):   
        return "Valid Email"
    else:   
        return None



@api_view(['POST'])
def register_user(request : Request):
    '''This function is designed to take only email and password, if the e-mail is valid, the username will
    take the same value of the email. Anyone can register using this function'''

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



@api_view(['GET'])
def users_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        user = User.objects.filter(username__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        user = User.objects.order_by("-id").all()[skip:get]

    data = UserSerilizer(user, many=True).data
    return Response(data, status=status.HTTP_200_OK)



@api_view(['PUT'])
def users_list(request: Request, user_id):
    try:
        user = User.objects.get(id = user_id)
        password = User.objects.get("password")
        print(user)
        print(password)
        data = UserpasswordSerilizer(instance=user, data=request.data)
        print(data)
        if data.is_valid():
            # data = hasher(data['password'])
            data.save()
            return Response({"msg" : "user password updated successfully "}, status=status.HTTP_200_OK)
        else:
            return Response({"msg" : "couldn't update the password", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"msg" : f"The user with ID No:{user_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_password(request : Request, user_id):
    try:
        user = User.objects.get(id = user_id)

        password = request.data["password"]

        user = User.objects.get(id=user_id)

        user.password = hasher(password.encode('utf-8'))
        user.save()

        return Response({"msg" : "user password updated successfully, saved as a hash password !!!"}, status=status.HTTP_200_OK)
    except Exception:
        return Response({"msg" : f"The user with ID No:{user_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)
