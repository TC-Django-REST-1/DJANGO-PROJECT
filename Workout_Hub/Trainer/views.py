from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import TrainerSerializer, CourseSerializer
from rest_framework import status
from .models import Trainer, Course


from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.

@api_view(['POST'])
def create_account(request : Request):
    #request.data["tr_name"] = request.data.get("username")
    #request.data["tr_email"] = request.data.get("email")
    #request.data["tr_password"] = request.data.get("password")

    trainers = TrainerSerializer(data=request.data)

    try:
        if trainers.is_valid():
            user = User.objects.create_user(trainers)
            user.save()
        #user = User.objects.create_user(username, email, password)
        #user.save()
    except Exception as e:
        return Response({"msg" : "Couldn't Create user", "error" : e})

    return Response({"msg" : "User Created Successfuly"}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def login(request : Request):

    username_from_client = request.data.get("username")
    password_from_client = request.data.get("password")

    user = authenticate(request, username=username_from_client, password=password_from_client)

    if user is None:
        return Response({"msg" : "user not found. Please check your credentials"}, status=status.HTTP_403_FORBIDDEN)
    
    token = AccessToken.for_user(user)

    return Response({"msg" : "You are authenticated successfully!", "token" : str(token)})

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request : Request):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Trainer.add_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    #request.data["c_trainer"] = user.id
    name = request.data["name"]
    ctype = request.data["type"]
    duration = request.data["duration"]
    price = request.data["price"]

    new_book = Book(c_trainer = user.id, c_name = name, c_type = ctype, c_duration = duration, c_price = price)
    new_book.save()

    return Response({"msg" : "Course created Successfully"}, status = stat.HTTP_201_CREATED)



@api_view(["GET"])
def view_courses(request : Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_courses = Book.objects.filter(title__contains=search_phrase)[skip:get]
    else:
        all_courses = Book.objects.all().order_by('-price')[skip:get]

    all_courses_list =  CourseSerializer(all_courses, many=True).data

    return Response({"msg" : "list of all courses", "courses" : all_courses_list}, status=status.HTTP_200_OK)



@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_course(request: Request, course_id):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Trainer.update_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    c = Course.objects.get(id=course_id)
    data = CourseSerializer(instance=c, data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response({"msg": "Course updated succefully!"}, status=status.HTTP_200_OK)
    return Response({"msg" : "couldn't update", "errors" : data.errors})



@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_course(request: Request, course_id):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Trainer.delete_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    c = Course.objects.get(id=course_id)
    c.delete()

    return Response({"msg":"Course deleted succefully!"}, status=status.HTTP_200_OK)