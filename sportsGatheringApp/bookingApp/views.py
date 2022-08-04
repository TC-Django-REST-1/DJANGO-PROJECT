from datetime import datetime
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Place

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PlaceSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(["GET"])
def get_all_plaices(request : Request):

    plaices = Place.objects.all()

    if "notBooked" in request.query_params:
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        all_plaices = []
        for place in plaices:
            plaices_booking_date = place.bookedAt.strftime("%Y-%m-%d %H:%M:%S")
            if datetime.strptime(now, "%Y-%m-%d %H:%M:%S") > datetime.strptime(plaices_booking_date, "%Y-%m-%d %H:%M:%S"):
                all_plaices.append(PlaceSerializer(instance=place).data)

        return Response({"msg": "all plaices", "data": all_plaices},status=status.HTTP_200_OK)

    data = PlaceSerializer(instance=plaices, many=True).data
    return Response({"msg": "all plaices", "data":data },status=status.HTTP_200_OK)

@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_place(request : Request):
    user = request.user

    if not user.is_authenticated:
        return Response({"msg": "Please login"},status=status.HTTP_403_FORBIDDEN)
    
    if not user.has_perm('place.add_place'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    place_serializer = PlaceSerializer(data=request.data)
    if place_serializer.is_valid():
        place_serializer.save()
    else:
        return Response({
            'msg': "sorry couldn't create a Place",
            "errors": place_serializer.errors,
        },status=status.HTTP_403_FORBIDDEN)
    
    return Response({"msg": "place was added successfully!"},status=status.HTTP_200_OK)

@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_place(request : Request, place_id):
    user = request.user

    if not user.is_authenticated:
        return Response({"msg": "Please login"},status=status.HTTP_403_FORBIDDEN)
    
    if not user.has_perm('place.change_place'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        place = Place.objects.get(id= place_id)
    except  Exception as e:
        return Response({"msg" : "This Place is not found"}, status=status.HTTP_404_NOT_FOUND)
        
    place = PlaceSerializer(instance=place ,data=request.data)
    if place.is_valid():
        place.save()
    else:
        return Response({
            'msg': "sorry couldn't update a Place",
            "errors": place.errors,
        },status=status.HTTP_403_FORBIDDEN)
    
    return Response({"msg": "place was updated successfully!"},status=status.HTTP_200_OK)

@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_place(request : Request, place_id):
    user = request.user

    if not user.is_authenticated:
        return Response({"msg": "Please login"},status=status.HTTP_403_FORBIDDEN)
    
    if not user.has_perm('place.delete_place'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        place = Place.objects.get(id= place_id)
    except  Exception as e:
        return Response({"msg" : "This Place is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    place.delete()

    return Response({"msg": "The Place deleted successfully!"}, status=status.HTTP_200_OK)