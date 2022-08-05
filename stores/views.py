from django.shortcuts import render
from .serializer import StoresSerializer, ProductsSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from django.urls import is_valid_path
from .models import Stores, Products
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

## STORES ##
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_store(request : Request):
  try:
    user = request.user
    if not user.has_perm('stores.add_stores'):
      return Response({"msg" : "Access denied! You don't have Products control permission."}, status=401)
    store_serializer = StoresSerializer(data= request.data)
    if not store_serializer.is_valid():
      raise Exception()
    store_serializer.save()
    return Response({"msg" : "Store added successfully!"}, status=201)
  except Exception as e:
    return Response({"msg" : "Something went wrong :|", "err" : store_serializer.errors}, status=403)

@api_view(['GET'])
def list_stores(request : Request):
  skip = int(request.query_params.get("skip", 0))
  get = int(request.query_params.get("get", 10))
  if "search" in request.query_params:
    search_phrase = request.query_params["search"]
    stores = Stores.objects.filter(store_name__startswitch=search_phrase)[skip:get]
  else:
    stores = Stores.objects.all()
  return Response({
    "msg" : "List of all stores",
    "stores" : StoresSerializer(instance=stores, many=True).data
  })

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_store(request : Request, store_id):
  try:
    user = request.user
    if not user.has_perm('stores.change_stores'):
      return Response({"msg" : "Access denied! You don't have Products control permission."}, status=401)
    store = Stores.objects.get(id = store_id)
    store_serializer = StoresSerializer(instance=store, data=request.data)
    if store_serializer.is_valid():
      store_serializer.save()
    else:
      return Response({"msg" : "Something went wrong :|", "err" : store_serializer.errors})
    return Response({"msg" : "Store updated successfully!"})
  except Exception as e:
    return Response({"msg" : "Store not found!"}, status=404)
  
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_store(request : Request, store_id):
  try:
    user = request.user
    if not user.has_perm('stores.delete_stores'):
      return Response({"msg" : "Access denied! You don't have Products control permission."}, status=401)
    store = Stores.objects.get(id = store_id)
    store.delete()
  except Exception as e:
    return Response({"msg" : "Store not found!"}, status=404)
  return Response({"msg" : f"{store.store_name} deleted successfully!"})

## PRODUCTS ##
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_product(request : Request):
  try:
    user = request.user
    if not user.has_perm('stores.add_products'):
      return Response({"msg" : "Access denied! You don't have Products control permission."}, status=401)
    product_serializer = ProductsSerializer(data= request.data)
    if not product_serializer.is_valid():
      raise Exception()
    product_serializer.save()
    return Response({"msg" : "Product added successfully!"}, status=201)
  except Exception as e:
    return Response({"msg" : "Something went wrong :|", "err" : product_serializer.errors}, status=403)


@api_view(['GET'])
def list_products(request : Request):
  skip = int(request.query_params.get("skip", 0))
  get = int(request.query_params.get("get", 10))
  if "search" in request.query_params:
    search_phrase = request.query_params["search"]
    products = Products.objects.filter(product_name__startswitch=search_phrase)[skip:get]
  else:
    products = Products.objects.all()
  return Response({
    "msg" : "List of all products",
    "products" : ProductsSerializer(instance=products, many=True).data
  })

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_product(request : Request, product_id):
  try:
    user = request.user
    if not user.has_perm('stores.change_products'):
      return Response({"msg" : "Access denied! You don't have Products control permission."}, status=401)
    product = Products.objects.get(id = product_id)
    product_serializer = ProductsSerializer(instance=product, data=request.data)
    if product_serializer.is_valid():
      product_serializer.save()
    else:
      return Response({"msg" : "Something went wrong :|", "err" : product_serializer.errors})
    return Response({"msg" : "Product updated successfully!"})
  except Exception as e:
    return Response({"msg" : "Product not found!"}, status=404)

@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_product(request : Request, product_id):
  try:
    user = request.user
    if not user.has_perm('stores.delete_products'):
      return Response({"msg" : "Access denied! You don't have Products control permission."}, status=401)
    product = Products.objects.get(id = product_id)
    product.delete()
  except Exception as e:
    return Response({"msg" : "Product not found!"}, status=404)
  return Response({"msg" : f"{product.product_name} deleted successfully!"})