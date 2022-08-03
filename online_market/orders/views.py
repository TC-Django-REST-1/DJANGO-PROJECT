from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['POST'])
def create(request: Request):
    return Response(
        {
            "msg": "Not Implemented"
        },
        status=status.HTTP_404_NOT_FOUND
    )


@api_view(['GET'])
def read(request: Request):
    return Response(
        {
            "msg": "Not Implemented"
        },
        status=status.HTTP_404_NOT_FOUND
    )


@api_view(['PUT'])
def update(request: Request):
    return Response(
        {
            "msg": "Not Implemented"
        },
        status=status.HTTP_404_NOT_FOUND
    )


@api_view(['DELETE'])
def delete(request: Request):
    return Response(
        {
            "msg": "Not Implemented"
        },
        status=status.HTTP_404_NOT_FOUND
    )
