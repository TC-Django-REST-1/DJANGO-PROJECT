from itertools import product
from multiprocessing import AuthenticationError
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Product, Category, Company,Comment
from .serializers import CategorySerializer, CommentSerializer, ProductSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_company(request : Request):
    name = request.data["name"]
    description= request.data["description"]

    new_company = Company(name=name, description=description)
    new_company.save()

    res_data = {
        "msg" : "Created new name company Successfully"
    }

    return Response(res_data)


@api_view(["DELETE"])
def delete_company(request : Request, company_id):

    try:
        company = Company.objects.get(id=company_id)
        company.delete()
    except Exception as e:
        return Response({"msg" : "The Company name is not Found!"})

    return Response({"msg" : f"delete the following company {company.title}"})


@api_view(['PUT'])
def update_company(request : Request, company_id):
    name = request.data["name"]
    description= request.data["description"]

    company = Company.objects.get(id=company_id)

    company.name = name
    company.description = description

    company.save()

    return Response({"msg" : "The Data of the company is updated !"})


@api_view(['POST'])
def add_category(request : Request):

    category_serializer = CategorySerializer(data=request.data)

    if CategorySerializer.is_valid():
        CategorySerializer.save()
    else:
        return Response({'msg' : 'could not add a new category', 'errors': category_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({'msg' : 'category added successfully!'}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_category(request : Request) -> Response :

    category = Category.objects.order_by('-id').all()

    try:

        category = CategorySerializer(category, many=True).data

        return Response(category, status=status.HTTP_200_OK)

    except Exception as e:

      return Response({"msg" : "rejected request please check your entities"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_product(request : Request) -> Response : 

    product_serializer = ProductSerializer(data=request.data)

    if product_serializer.is_valid():

        try:
            product_serializer.save()
            return Response({"msg" : "product added succefully!"}, status=status.HTTP_201_CREATED)

        except Exception as e:

            return Response({"msg" : "coudn't add the product, try again", 'error' : e},status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : product_serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_product(request : Request, product_id : int) -> Response :

    if type(product_id) == int: 
        product = product.objects.get(id=product_id)
        product_ser = ProductSerializer(instance=product, data=request.data)
        if product_ser.is_valid():
            print(product_ser)
            product_ser.save()
            return Response({"msg" : "product updated succefully"}, status=status.HTTP_201_CREATED)

        else:
            return Response({"msg" : "couldn't update it succefully, try again"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : "server issue"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def list_product(request : Request) -> Response :

    product = Product.objects.order_by('-id').all()

    try:

        products = ProductSerializer(product, many=True).data

        return Response(products, status=status.HTTP_200_OK)

    except Exception as e:

      return Response({"msg" : "rejected request please check your entities"}) 






#comment
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_comment(request : Request):

    user_id = request.user.id

    request.data["user"] = user_id

    comment_serializer = CommentSerializer(data=request.data)

    if comment_serializer.is_valid():
        comment_serializer.save()
    else:
        return Response({"msg" : "couldn't create a comment", "errors" : comment_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "Comment Added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_comments(request : Request):

    if "book_id" in request.query_params:
        comments = Comment.objects.filter(book=request.query_params["book_id"])
    else:
        comments = Comment.objects.all()

    comments_data = CommentSerializer(instance=comments, many=True).data

    return Response({"msg" : "list of all comments", "comments" : comments_data})




@api_view(['PUT'])
def update_comment(request : Request, comment_id):

    try:
        comment = Comment.objects.get(id=comment_id)
    except Exception as e:
        return Response({"msg" : "This comment is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    comment_serializer = CommentSerializer(instance=comment, data=request.data)

    if comment_serializer.is_valid():
        comment_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : comment_serializer.errors})

    return Response({"msg" : "Comment updated successfully"})