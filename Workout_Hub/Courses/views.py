from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import CoursesSerializer
from rest_framework import status
from .models import Courses

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.
@api_view(["GET"])
def view_courses(request : Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_courses = Courses.objects.filter(title__contains=search_phrase)[skip:get]
    else:
        all_courses = Courses.objects.all().order_by('-price')[skip:get]

    all_courses_list =  CoursesSerializer(all_courses, many=True).data

    return Response({"msg" : "list of all courses", "courses" : all_courses_list}, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request : Request):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Courses.add_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    #request.data["c_trainer"] = user.id
    name = request.data["name"]
    ctype = request.data["type"]
    duration = request.data["duration"]
    price = request.data["price"]

    new_course = Courses(c_trainer = user.id, c_name = name, c_type = ctype, c_duration = duration, c_price = price)
    new_course.save()

    return Response({"msg" : "Course created Successfully"}, status = stat.HTTP_201_CREATED)


@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_course(request: Request, course_id):
    #authenticated user info is stored in request.user
    user = request.user
    
    if not user.has_perm('Courses.update_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    c = Courses.objects.get(id=course_id)
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

    c = Courses.objects.get(id=course_id)
    c.delete()

    return Response({"msg":"Course deleted succefully!"}, status=status.HTTP_200_OK)