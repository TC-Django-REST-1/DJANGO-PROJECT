from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Category, Task, Comment
from .serializers import CategorySerializers, TaskSerializers, CommentSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

# Category CRUD
@api_view(["GET"])
def list_category(request: Request):

    Categories = Category.objects.all()
    ctgry_data = CategorySerializers(instance=Categories, many=True).data

    return Response({"msg": "List of all categories", "Categories": ctgry_data}, status=status.HTTP_200_OK)



@api_view(["POST"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def create_category(request: Request):
    
    # user = request.user
    # if not user.is_authenticated:
    #     return Response({"msg" : "Please Log In"}, status=status.HTTP_401_UNAUTHORIZED)
    # if not user.has_perm('memos.create_category'):
    #     return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    # request.data['user'] = user

    cate_serializer = CategorySerializers(data=request.data)

    if cate_serializer.is_valid():
        cate_serializer.save()
    else:
        return Response({"msg": "Category could not be created!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "Category have been created successfully"}, status=status.HTTP_201_CREATED)



@api_view(["PUT"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def update_category(request: Request, cate_id):
    try:
        category = Category.objects.get(id=cate_id)
    except Exception as e:
        return Response({"msg": "This category does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    cate_serializer = CategorySerializers(instance=category, data=request.data)
    if cate_serializer.is_valid():
        cate_serializer.save()
    else:
        return Response({"msg": "Category could not be modified!"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg": "Category have been modified successfully"}, status=status.HTTP_200_OK)



@api_view(["DELETE"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def del_category(request: Request, cate_id):

    try:
        category = Category.objects.get(id=cate_id)
        category.delete()
    except Exception as e:
        return Response({"msg": "This category does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({"msg": "Category have been deleted successfully"}, status=status.HTTP_200_OK)




# Task CRUD
@api_view(["GET"])
def list_task(request: Request):

    tasks = Task.objects.all()
    tasks_data = TaskSerializers(instance=tasks, many=True).data

    return Response({"msg": "List of all tasks", "Tasks": tasks_data}, status=status.HTTP_200_OK)



@api_view(["POST"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def add_task(request: Request):

    task_serializer = TaskSerializers(data=request.data)

    if task_serializer.is_valid():
        task_serializer.save()
    else:
        return Response({"msg": "Task could not be added!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "Task have been added successfully"}, status=status.HTTP_202_ACCEPTED)



@api_view(["PUT"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def update_task(request: Request, task_id):

    try:
        task = Task.objects.get(id=task_id)
    except Exception as e:
        return Response({"msg": "This task does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    task_serializer =TaskSerializers(instance=task, data=request.data)
    if task_serializer.is_valid():
        task_serializer.save()
    else:
        return Response({"msg": "Task could not be modified!"}, status=status.HTTP_400_BAD_REQUEST)
        
    return Response({"msg": "Task have been modified successfully"}, status=status.HTTP_200_OK)



@api_view(["DELETE"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def del_task(request: Request, task_id):

    try:
        task = Task.objects.get(id=task_id)
        task.delete()
    except:
        return Response({"msg": "This is task does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({"msg": "Task have been deleted successfully"}, status=status.HTTP_200_OK)




#  Comment CRUD
@api_view(["GET"])
def list_comment(request: Request):

    list_comment = Comment.objects.all()
    comment_data = CommentSerializer(instance=list_comment, many=True).data

    return Response({"msg": "List of all comments", "Comments": comment_data}, status=status.HTTP_200_OK)



@api_view(["POST"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def add_comment(request: Request):

    comment_serializer = CommentSerializer(data=request.data)

    if comment_serializer.is_valid():
        comment_serializer.save()
    else:
        return Response({"msg": "Comment could not be added!", "errors": comment_serializer.errors})
    
    return Response({"msg": "Comment have been added successfully"}, status=status.HTTP_202_ACCEPTED)



@api_view(["PUT"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def update_comment(request: Request, cmnt_id):

    try:
        comment = Comment.objects.get(id=cmnt_id)
    except:
        return Response({"msg": "This comment does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    comment_serializer = CommentSerializer(instance=comment, data=request.data)
    if comment_serializer.is_valid():
        comment_serializer.save()
    else:
        return Response({"msg": "Comment could not be modified!"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg": "Comment have been modified successfully"}, status=status.HTTP_200_OK)



@api_view(["DELETE"])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
def del_comment(request: Request, cmnt_id):

    try:
        comment = Comment.objects.get(id=cmnt_id)
        comment.delete()
    except:
        return Response({"msg": "This comment does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg": "Comment have been deleted successfully"}, status=status.HTTP_200_OK)