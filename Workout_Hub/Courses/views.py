from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .seriallizers import CoursesSerializer
from rest_framework import status
from .models import Course
from Users.models import Trainers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.
@api_view(["GET"])
def view_courses(request : Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_courses = Course.objects.filter(title__contains=search_phrase)[skip:get]
    else:
        all_courses = Course.objects.all().order_by('-c_price')[skip:get]

    all_courses_list =  CoursesSerializer(all_courses, many=True).data

    return Response({"msg" : "list of all courses", "courses" : all_courses_list}, status=status.HTTP_200_OK)



@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def register_trainee(request : Request, trainee_id):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Courses.register_trainee'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        request.data["c_trainee"] = trainee_id

    except Exception as e:
        return Response({"msg" : "Couldn't regiter the trainee", "error" : e})

    return Response({"msg" : "trainee regitered Successfully"}, status = stat.HTTP_201_CREATED)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request : Request):
    #authenticated user info is stored in request.user
    user = request.user
    tid = user.pk
    print("tid ",tid)

    if not user.has_perm('Courses.add_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    request.data["c_trainer"] = tid
    new_course = CoursesSerializer(data=request.data)
    if new_course.is_valid():
        new_course.save()
    else:
        return Response({"msg" : "couldn't add a course", "errors" : new_course.errors}, status=status.HTTP_403_FORBIDDEN)


    return Response({"msg" : "Course created Successfully"}, status = status.HTTP_201_CREATED)


@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_course(request: Request, course_id):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Courses.update_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    c = Course.objects.get(id=course_id)
    data = CoursesSerializer(instance=c, data=request.data,partial=True)

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
    
    if not user.has_perm('Courses.delete_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    c = Course.objects.get(id=course_id)
    c.delete()

    return Response({"msg":"Course deleted succefully!"}, status=status.HTTP_200_OK)