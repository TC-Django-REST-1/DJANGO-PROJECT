from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .seriallizers import CoursesSerializer
from rest_framework import status
from .models import Course
from Users.models import Trainers,Trainees

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



@api_view(["PATCH"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def register_trainee(request : Request, trainee_id):
    #authenticated user info is stored in request.user
    #user = request.user
    
    #if not user.has_perm('Courses.change_trainees'):
        #return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        #request.data["c_trainee"] = Trainees.objects.get(pk=trainee_id)
        #name = request.data["c_name"]
        #trainee_id = request.data["c_trainee"]
        c_trainee = Trainees.objects.get(pk=trainee_id)
        name =request.data["c_name"]
        c = Course.objects.get(c_name=name)
        print(c_trainee)
        c.c_trainee.add(c_trainee)
        c.save()

    except Exception as e:
        return Response({"msg" : "Couldn't regiter the trainee", "error" : str(e)})

    return Response({"msg" : "trainee regitered Successfully"}, status = status.HTTP_201_CREATED)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request : Request, trainer_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.has_perm('Courses.add_course'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    request.data["c_trainer"] = trainer_id
    new_course = CoursesSerializer(data=request.data)
    if new_course.is_valid():
        new_course.save()
    else:
        return Response({"msg" : "couldn't add a course", "errors" : new_course.errors}, status=status.HTTP_403_FORBIDDEN)


    return Response({"msg" : "Course created Successfully"}, status = status.HTTP_201_CREATED)


@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def course_update(request : Request, course_id):
 
    try:
        c = Course.objects.get(pk=course_id)
        data = CoursesSerializer(instance=c, data=request.data,partial=True)

        if data.is_valid():
            data.save()
        else:
            return Response({"msg" : "couldn't update", "errors" : data.errors})

    except Exception as e:
        return Response({"msg" : "couldn't find the course"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg": "Course updated succefully!"}, status=status.HTTP_200_OK)


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