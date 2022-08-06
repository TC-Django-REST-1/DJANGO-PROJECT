from .serializers import CafeSerializer, ProductSerializer 
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from .models import Cafe, Product
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here  
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_cafe(request : Request):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.add_cafe'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    cafeSerializer = CafeSerializer(data=request.data)
    if cafeSerializer.is_valid():
        cafeSerializer.save()
    else:
        return Response({"msg" : "opps!  cafe could not created", "error": cafeSerializer.errors},status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "cafe Added Successfully!"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_product(request : Request):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.add_product'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)

    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "opps!  product could not created", "error": product_serializer.errors},status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Product Added Successfully!"},status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

def list_cafe(request:Request):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.view_cafe'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 5))
    
    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        cafes = Cafe.objects.filter(title=search_phrase)[skip:get]
    else:
        cafes = Cafe.objects.all()[skip:get]
    cafe = CafeSerializer(instance=cafes, many=True).data

    return Response({"msg" : "List All cafes ","Cafe" : cafe}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_product(request:Request):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.view_product'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 5))

    products = Product.objects.all()[skip:get]
    product = ProductSerializer(instance=products, many=True).data

    return Response({"msg" : "List All products ", "product" : product}, status=status.HTTP_200_OK)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_cafe(request:Request, cafe_id):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.change_cafe'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        cafe = Cafe.objects.get(id = cafe_id)
    except Exception :
        return Response({"msg" : "opss! cafe is not found"}, status=status.HTTP_404_NOT_FOUND)

    cafe_ser = CafeSerializer(instance=cafe, data=request.data)

    if cafe_ser.is_valid():
        cafe_ser.save()
    else:
        return Response({"msg" : "opss! cafe Couldn't update", "errors" : cafe_ser.errors})

    return Response({"msg" : "cafe updated successfully"})

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_product(request:Request,product_id):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.change_product'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        product = Product.objects.get(id = product_id)
    except Exception :
        return Response({"msg" : "opss! product is not found"}, status=status.HTTP_404_NOT_FOUND)

    product_ser = ProductSerializer(instance=product, data=request.data)

    if product_ser.is_valid():
        product_ser.save()
    else:
        return Response({"msg" : "opss! product Couldn't update", "errors" : product_ser.errors})

    return Response({"msg" : "Product updated successfully"})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_cafe(request:Request, cafe_id):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.delete_cafe'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    cafe = Cafe.objects.get(id = cafe_id)
    cafe.delete()
    return Response({"msg" : "cafe Deleted successfully!"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_product(request:Request, product_id):
    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"},status=status.HTTP_403_FORBIDDEN)
    if not user.has_perm('cafes.delete_product'):
        return Response({"msg" : "you dont have permission!"},status=status.HTTP_401_UNAUTHORIZED)
    product = Product.objects.get(id =product_id)
    product.delete()
    return Response({"msg" : "Product Deleted successfully!"}, status=status.HTTP_200_OK)
