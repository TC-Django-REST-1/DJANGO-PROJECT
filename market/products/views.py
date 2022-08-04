from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from stores.models import Customers

# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request: Request, Customers_id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('products.add_product'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
       Customers= Customers.objects.get(id=Customers_id)
    except Exception as e:
        return Response(
            {
                "msg": "Store not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if not Customers.owner.id == user.id:
        return Response(
            {
                "msg": "You are not the Customers owner.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    product_serializer = ProductSerializer(data=request.data)
    product_serializer.set_Customers(Customers)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": product_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": f"Product created with id {product_serializer.data['id']}."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def read(request: Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_products = Product.objects.filter(
            title__startswith=search_phrase)[skip:get]
    else:
        all_products = Product.objects.all()[skip:get]

    return Response(
        {
            "msg": 'list of products',
            "products": ProductSerializer(instance=all_products, many=True).data,
            "count": len(all_products)
        },
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request: Request, product_id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('products.add_product'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        product = Product.objects.get(id=product_id)
        Customers = Customers.objects.get(id=product.Customerse.id)
    except Exception as e:
        return Response(
            {
                "msg": "product not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if not store.owner.id == user.id:
        return Response(
            {
                "msg": "You are not the Customers owner.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    product_serializer = ProductSerializer(instance=product, data=request.data)
    product_serializer.set_store(Customers)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": product_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "Product updated."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request: Request, product_id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('stores.change_Customers'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        product = Product.objects.get(id=product_id)
        Customers = Customers.objects.get(id=product.Customers.id)
        if not user.id == Customers.owner.id:
            return Response(
                {
                    "msg": "You are not the Customers owner.",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        product.delete()
    except Exception as e:
        return Response(
            {
                "msg": "Product not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            "msg": "Product deleted."
        },
        status=status.HTTP_200_OK
    )