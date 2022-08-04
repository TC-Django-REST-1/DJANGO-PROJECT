from urllib import response
from urllib.request import Request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

students_list = [
{"name":"ghassan"},
{"name":"hussam"}
]

@api_view(['GET'])
def display(request : Request):
    response_data = {
        "msg": "list of students",
        "students" : students_list
    }
    return Response(students_list)


@api_view(["POST"])
def add_student(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    name = request.data["name"]
    new_student = students_list(name=name)
    new_student.save()

    res_data = {
        "msg" : "student add Successfully"
    }

    return Response(res_data)

@api_view(['PUT'])
def update_student(request : Request, students_list):

    name = request.data["name"]
    

    student = students_list.objects.get(id=student)

    student.title = name
    student.save()

    return Response({"msg" : "student is updated !"})


@api_view(["DELETE"])
def delete_student(request : Request, student_id):

    try:
        student = students_list.objects.get(id=student)
        student.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})

    return Response({"msg" : f"delete the following student {student.name}"})


teachers_list = [
{"name":"ahmed"},
{"name":"khalid"}
]

@api_view(['GET'])
def display_teachers(request : Request):
    response_data = {
        "msg": "list of teachers",
        "students" : teachers_list
    }
    return Response(teachers_list)


@api_view(["POST"])
def add_teachers(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    name = request.data["name"]
    new_teachers = teachers_list(name=name)
    new_teachers.save()

    res_data = {
        "msg" : "teachers add Successfully"
    }

    return Response(res_data)

@api_view(['PUT'])
def update_teachers(request : Request, teachers_list):

    name = request.data["name"]
    

    teachers = teachers_list.objects.get(id=teachers)

    teachers.title = name
    teachers.save()

    return Response({"msg" : "teachers is updated !"})


@api_view(["DELETE"])
def delete_teachers(request : Request, teachers_id):

    try:
        teachers = teachers_list.objects.get(id=teachers)
        teachers.delete()
    except Exception as e:
        return Response({"msg" : "The teachers is not Found!"})

    return Response({"msg" : f"delete the following student {teachers.name}"})