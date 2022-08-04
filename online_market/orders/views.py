from products.models import Product
from .serializers import OrderSerializer, OrderProductSerializer
from .models import Order, OrderProduct
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request: Request):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.add_order'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    order_serializer = OrderSerializer(data=request.data)
    order_serializer.set_customer(request)
    if order_serializer.is_valid():
        order_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": order_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": f"Order created with id {order_serializer.data['id']}."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def read(request: Request):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.view_order'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "order_id" in request.query_params:
        id = request.query_params["order_id"]
        all_orders = Order.objects.filter(id=id)[skip:get]
    else:
        all_orders = Order.objects.all()[skip:get]

    return Response(
        {
            "msg": 'list of orders',
            "orders": OrderSerializer(instance=all_orders, many=True).data,
            "count": len(all_orders)
        },
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request: Request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Exception as e:
        return Response(
            {
                "msg": "Order not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.change_order'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.id == order.customer.id:
        return Response(
            {
                "msg": "You did not make this order.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    order_serializer = OrderSerializer(instance=order, data=request.data)
    order_serializer.set_customer(request)
    if order_serializer.is_valid():
        order_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": order_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "Order updated."
        },
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request: Request, order_id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.delete_order'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        order = Order.objects.get(id=order_id)
        if not user.id == order.customer.id:
            return Response(
                {
                    "msg": "You did not make this order.",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        order.delete()
    except Exception as e:
        return Response(
            {
                "msg": "Order not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            "msg": "Order deleted."
        },
        status=status.HTTP_200_OK
    )

################################################
################################################
# ORDER PRODUCT
################################################
################################################


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_order_product(request: Request):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.add_orderproduct'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    order_product_serializer = OrderProductSerializer(data=request.data)
    if order_product_serializer.is_valid():
        order_product_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": order_product_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": f"OrderProduct created with id {order_product_serializer.data['id']}."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def read_order_product(request: Request):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.view_orderproduct'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "order_product_id" in request.query_params:
        id = request.query_params["order_product_id"]
        all_order_products = OrderProduct.objects.filter(id=id)[skip:get]
    else:
        all_order_products = OrderProduct.objects.all()[skip:get]

    return Response(
        {
            "msg": 'list of orderProducts',
            "orderProducts": OrderProductSerializer(instance=all_order_products, many=True).data,
            "count": len(all_order_products)
        },
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_order_product(request: Request, order_product_id):
    try:
        order_product = OrderProduct.objects.get(id=order_product_id)
    except Exception as e:
        return Response(
            {
                "msg": "OrderProduct not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.change_orderproduct'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.id == order_product.order.customer.id:
        return Response(
            {
                "msg": "You did not make this orderProduct.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    order_product_serializer = OrderProductSerializer(
        instance=order_product, data=request.data)
    if order_product_serializer.is_valid():
        order_product_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": order_product_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "OrderProduct updated."
        },
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_order_product(request: Request, order_product_id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('orders.delete_order'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        order_product = OrderProduct.objects.get(id=order_product_id)
        if not user.id == order_product.order.customer.id:
            return Response(
                {
                    "msg": "You did not make this orderProduct.",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        order_product.delete()
    except Exception as e:
        return Response(
            {
                "msg": "OrderProduct not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            "msg": "OrderProduct deleted."
        },
        status=status.HTTP_200_OK
    )
