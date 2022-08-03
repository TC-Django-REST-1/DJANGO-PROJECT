from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Category, Task, Comment

# Create your views here.

# Category CRUD
@api_view(["GET"])
def list_category(request: Request):

    list_category = Category.objects.all()
    cate_data = CategorySerializers(instance=Category, many=True).data

    return Response({"msg": "Categories displayed successfully"}, status=status.HTTP_200_OK)



@api_view(["POST"])
def create_category(request: Request):

    cate_serializer = CategorySerializers(data=request.data)

    if cate_serializer.is_valid():
        cate_serializer.save()
    else:
        return Response({"msg": "Category could not be created!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "Category have been created successfully"}, status=status.HTTP_201_CREATED)



@api_view(["PUT"])
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
def del_category(request: Request, cate_id):

    try:
        category = category.objects.get(id=cate_id)
    except Exception as e:
        return Response({"msg": "This category does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    cate_serializer = CategorySerializers(instance=category, data=request.data)
    if cate_serializer.is_valid():
        cate_serializer.delete()
    else:
        return Response({"msg": "Category could not be deleted!"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg": "Category have been deleted successfully"}, status=status.HTTP_200_OK)




# Task CRUD
api_view(["GET"])
def list_task(request: Request):

    list_tasks = Task.objects.all()
    tasks_data = TaskSerializers(instance=list_tasks, many=True).data

    return Response({"msg": "Tasks displayed successfully"}, status=status.HTTP_200_OK)



@api_view(["POST"])
def add_task(request: Request):

    task_serializer = TaskSerializers(data=request.data)

    if task_serializer.is_valid():
        task_serializer.save()
    else:
        return Response({"msg": "Task could not be added!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "Task have been added successfully"}, status=status.HTTP_202_ACCEPTED)



@api_view(["PUT"])
def update_task(request: Request, task_id):

    try:
        task = Task.objects.get(id=task_id)
    except:
        return Response({"msg": "This task does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    if task.is_valid():
        task.save()
    else:
        return Response({"msg": "Task could not be modified!"}, status=status.HTTP_400_BAD_REQUEST)
        
    return Response({"msg": "Task have been modified successfully"}, status=status.HTTP_200_OK)



@api_view(["DELETE"])
def del_task(request: Request, task_id):

    try:
        task = Task.objects.get(id=task_id)
    except:
        return Response({"msg": "This is task does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    task_serializer = TaskSerializers(instance=task, data=request.data)
    if task_serializer.is_valid():
        task_serializer.delete()
    else:
        return Response({"msg": "Task could not be deleted"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "Task have been deleted successfully"}, status=status.HTTP_200_OK)




#  Comment CRUD
@api_view(["GET"])
def list_comment(request: Request):

    list_comment = Comment.objects.all()
    comment_data = CommentSerializer(instance= list_comment, many=True).data

    return Response({"msg": "Comment displayed successfully"}, status=status.HTTP_200_OK)



@api_view(["POST"])
def add_comment(request: Request):

    comment_serializer = CommentSerializer(data=request.data)

    if comment_serializer.is_valid():
        comment_serializer.save()
    else:
        return Response({"msg": "Comment could not be added!", "errors": comment_serializer.errors})
    
    return Response({"msg": "Comment have been added successfully"}, status=status.HTTP_202_ACCEPTED)



@api_view(["PUT"])
def update_comment(request: Request, cmnt_id):

    try:
        comment = Comment.objects.get(id=cmnt_id)
    except:
        return Response({"msg": "This comment does not exist!"}, status=status.HTTP_404_NOT_FOUND)
    
    if comment.is_valid():
        comment.save()
    else:
        return Response({"msg": "Comment could not be modified!"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg": "Comment have been modified successfully"}, status=status.HTTP_200_OK)



@api_view(["DELETE"])
def del_comment(request: Request, cmnt_id):

    try:
        comment = Comment.objects.get(id=cmnt_id)
    except:
        return Response({"msg": "This comment does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    comment_data = CommentSerializer(instance=comment, data=request.data)
    if comment_serializer.is_valid():
        comment_serializer.delete()
    else:
        return Response({"msg": "Comment could not be deleted"}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"msg": "Comment have been deleted successfully"}, status=status.HTTP_200_OK)