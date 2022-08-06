from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import exercise
from .serializers import ExerciseSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_exercise(request : Request):
    
    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if not request.user.groups.filter(name = "coachs").exists():
        return Response({"msg" : "Only coachs can add an exercise."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    request.data["coach"] = request.user.id
    excer_ser = ExerciseSerializer(data=request.data)
    
    if excer_ser.is_valid():
        excer_ser.save()
    else:
        return Response({"msg" : "Exercise couldn't be created.", "errors" : ExerciseSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Exercise created Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_exercises(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Coach can only list the excersises he created.
    if request.user.groups.filter(name = "coachs").exists():
        excer = exercise.objects.filter(coach=request.user.id)
        excer_data = ExerciseSerializer(instance=excer, many=True).data
    
    # Trainees can list all excersises.
    if request.user.groups.filter(name = "trainees").exists():
        excer = exercise.objects.all()
        excer_data = ExerciseSerializer(instance=excer, many=True).data

    if "skip" in request.query_params and "get" in request.query_params:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))

        excer = exercise.objects.all()[skip:get]
        excer_data = ExerciseSerializer(instance=excer, many=True).data
  
    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        excer = exercise.objects.filter(exercise_name=search_phrase)
        excer_data = ExerciseSerializer(instance=excer, many=True).data

    return Response({"msg" : "list of all exercises", "exercises" : excer_data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_exercise(request : Request, excer_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.user.groups.filter(name = "coachs").exists():
        return Response({"msg" : "Only coachs can edit an exercise."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        # Coach can only edit the excersises he created.
        excer_objs = exercise.objects.filter(coach=request.user.id)
        excer = excer_objs.get(id=excer_id)
    except:
        return Response({"msg" : "Exercise couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
    
    request.data["coach"] = request.user.id
    excer_ser = ExerciseSerializer(instance=excer, data=request.data)

    if excer_ser.is_valid():
        excer_ser.save()
    else:
        return Response({"msg" : "Exercise couldn't be updated", "errors" : ExerciseSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : "Exercise updated Successfully!"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
def delete_exercise(request : Request, excer_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.user.groups.filter(name = "coachs").exists():
        return Response({"msg" : "Only coachs can delete an exercise."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        # Coach can only delete the excersises he created.
        excer_objs = exercise.objects.filter(coach=request.user.id)
        excer = excer_objs.get(id=excer_id)
    except:
        excer_data = {
            "msg":"Fail to found exercise, please check provided id."
        }

        return Response(excer_data, status=status.HTTP_404_NOT_FOUND) 

    excer.delete()

    excer_data = {
            "msg":f"Exercise {excer.exercise_name} deleted Successfully!"
        }
    
    return Response(excer_data, status=status.HTTP_200_OK)