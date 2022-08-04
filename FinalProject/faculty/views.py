from urllib import response
from urllib.request import Request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

class_list = [
{"name":"math"},
{"name":"arabic"}
]

@api_view(['GET'])
def display(request : Request):
    response_data = {
        "msg": "list of classes",
        "students" : class_list
    }
    return Response(class_list)


@api_view(["POST"])
def add_class(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    name = request.data["name"]
    new_class = class_list(name=name)
    new_class.save()

    res_data = {
        "msg" : "class add Successfully"
    }

    return Response(res_data)

@api_view(['PUT'])
def update_class(request : Request, class_list):

    name = request.data["name"]
    

    student = class_list.objects.get(id=student)

    student.title = name
    student.save()

    return Response({"msg" : "student is updated !"})


@api_view(["DELETE"])
def delete_class(request : Request, class_id):

    try:
        class_ = class_list.objects.get(id=class_)
        class_.delete()
    except Exception as e:
        return Response({"msg" : "The student is not Found!"})

    return Response({"msg" : f"delete the following student {class_.name}"})
    
