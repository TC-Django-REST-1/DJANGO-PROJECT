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
def update_students(request : Request, students_list):

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