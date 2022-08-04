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
        "movies" : students_list
    }
    return Response(students_list)