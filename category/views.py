# from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


from .models import Brand, Product
from .serializer import SerializerBrand, SerializerProduct
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_brand(request : Request) -> Response :

    """ add new brand """

    brand = SerializerBrand(data=request.data)

    if brand.is_valid():

        try:

            brand.save()
            return Response({"msg" : "brand added succefully!"}, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response({"msg" : "coudn't add the brand, try again", 'error' : e},status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg" : brand.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def show_brand(request : Request) -> Response :

    brand = Brand.objects.order_by('-id').all()

    try:

        brands = SerializerBrand(brand, many=True).data
        
        return Response(brands, status=status.HTTP_200_OK)

    except Exception as e:

        return Response({"msg" : "rejected request please check your entities"})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_brand(request : Request, brand_id : int) -> Response :

    if type(brand_id) == int: 
        brand = Brand.objects.get(id=brand_id)
        brand_ser = SerializerBrand(instance=brand, data=request.data)
        if brand_ser.is_valid():
            print(brand_ser)
            brand_ser.save()
            return Response({"msg" : "brand updated succefully"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"msg" : "couldn't update it succefully, try again"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : "server issue"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_brand(request : Request, brand_id : int) -> Response :

    try:
        brand = Brand.objects.get(id=brand_id)
        print(brand)
        brand.delete()

    except Exception as e: 
        return Response({"msg" : "brand not found"}, status=status.HTTP_404_NOT_FOUND)


    return Response({"msg" : "brand deleted"}, status=status.HTTP_200_OK)


# Electronic


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_product(request : Request) -> Response : 

    product = SerializerProduct(data=request.data)

    if product.is_valid():

        try:
            product.save()
            return Response({"msg" : "product added succefully!"}, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response({"msg" : "coudn't add the product, try again", 'error' : e},status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg" : product.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def show_products(request : Request) -> Response :


    try:
        product = Product.objects.order_by('-id').all()

        products = SerializerProduct(product, many=True).data
        
        return Response(products, status=status.HTTP_200_OK)

    except Exception as e:

        return Response({"msg" : "rejected request please check your entities"})