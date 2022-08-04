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
def dis(request : Request):
    response_data = {
        "msg": "list of classes",
        "movies" : class_list
    }
    return Response(class_list)