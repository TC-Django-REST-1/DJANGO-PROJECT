from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import diet
from .serializers import DietSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def create_diet(request : Request):
    
    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if not request.user.groups.filter(name = "coachs").exists():
        return Response({"msg" : "Only coachs can add a diet."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    request.data["coach"] = request.user.id
    diet_ser = DietSerializer(data=request.data)
    
    if diet_ser.is_valid():
        diet_ser.save()
    else:
        return Response({"msg" : "Diet couldn't be created.", "errors" : DietSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Diet created Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_diets(request : Request):

    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Coach can only list the diets he created.
    if request.user.groups.filter(name = "coachs").exists():
        diets = diet.objects.filter(coach=request.user.id)
        diet_data = DietSerializer(instance=diets, many=True).data
    
    # Trainees can list all diets.
    if request.user.groups.filter(name = "trainees").exists():
        diets = diet.objects.all()
        diet_data = DietSerializer(instance=diets, many=True).data

    if "skip" in request.query_params and "get" in request.query_params:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))

        diets = diet.objects.all()[skip:get]
        diet_data = DietSerializer(instance=diets, many=True).data
  
    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        diets = diet.objects.filter(diet_name=search_phrase)
        diet_data = DietSerializer(instance=diets, many=True).data

    return Response({"msg" : "list of all diets", "diets" : diet_data}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_diet(request : Request, diet_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.user.groups.filter(name = "coachs").exists():
        return Response({"msg" : "Only coachs can edit a diet."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        # Coach can only edit the diets he created.
        diet_objs = diet.objects.filter(coach=request.user.id)
        diet_ = diet_objs.get(id=diet_id)
    except:
        return Response({"msg" : "Diet couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
    
    request.data["coach"] = request.user.id
    diet_ser = DietSerializer(instance=diet_, data=request.data)

    if diet_ser.is_valid():
        diet_ser.save()
    else:
        return Response({"msg" : "Diet couldn't be updated", "errors" : DietSerializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : "Diet updated Successfully!"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
def delete_diet(request : Request, diet_id):

    if not request.user.is_authenticated:
        return Response({"msg" : "Please login."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if not request.user.groups.filter(name = "coachs").exists():
        return Response({"msg" : "Only coachs can delete a diet."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        # Coach can only delete the diets he created.
        diet_objs = diet.objects.filter(coach=request.user.id)
        diet_ = diet_objs.get(id=diet_id)
    except:
        diet_data = {
            "msg":"Fail to found diets, please check provided id."
        }

        return Response(diet_data, status=status.HTTP_404_NOT_FOUND) 

    diet_.delete()

    diets_data = {
            "msg":f"Diet {diet_.diet_name} deleted Successfully!"
        }
    
    return Response(diets_data, status=status.HTTP_200_OK)