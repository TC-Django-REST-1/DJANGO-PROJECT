# from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


from .models import Order
from .serializer import SerializerOrder
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_order(request : Request) -> Response :

    """ add new order """
    request.data['user'] = request.user.id
    order = SerializerOrder(data=request.data)

    if order.is_valid():

        try:

            order.save()
            return Response({"msg" : "order added succefully. one more step to ship your order"}, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response({"msg" : "coudn't add the order, try again", 'error' : e},status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg" : order.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def cancel_order(request : Request, order_id : int) -> Response :

    """ delete order """


    try: 
        request.data['user'] = request.user.id
        order = Order.objects.get(id=order_id)
        order.delete()
        return Response({"msg": "order cancelled"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"msg":"order not found", "error": e}, status=status.HTTP_404_NOT_FOUND)




@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def show_orders(request : Request) -> Response:
    
    try:
        order = Order.objects.get(user=request.user.id)
        orders = SerializerOrder(order, many=True).data
        return Response(orders, status=status.HTTP_200_OK)

    except Exception as e:

        return Response({"msg" : "rejected request please check your entities"})
