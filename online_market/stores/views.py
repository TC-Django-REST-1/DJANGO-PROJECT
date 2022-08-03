from .serializers import StoreSerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['POST'])
def create(request: Request):
    store_serializer = StoreSerializer(data=request.data)
    if store_serializer.is_valid():
        store_serializer.save()
    else:
        return Response(
            {
                "msg": "Not Implemented",
                "error": store_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "Store created."
        },
        status=status.HTTP_201_CREATED
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
