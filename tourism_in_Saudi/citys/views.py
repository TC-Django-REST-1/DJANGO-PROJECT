from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status

from .models import City, Place
from .serializers import CitySerializer, PlaceSerializer

# Create your views here.

@api_view(['POST'])
def add_city(request: Request):
    city_serializer = CitySerializer(data=request.data)

    if city_serializer.is_valid():
        city_serializer.save()
    else: 
        return Response({"msg": "couldn't create city", "errors": city_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg": "city created successfuly!"}, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def list_city(request: Request):
    citys = City.objects.all()
    citys_data = CitySerializer(instance=citys, many=True).data

    return Response({"msg": "list of all citys", "citys": citys_data})


@api_view(["PUT"])
def update_city(request: Request, city_id):
    try:
        city = City.objects.get(id=city_id)
    except Exception as e:
        return Response({"msg": "This city does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    city_serializer = CitySerializer(instance=city, data=request.data)

    if city_serializer.is_valid():
        city_serializer.save()
    else: 
        return Response({"msg": "couldn't update", "errors": city_serializer.errors})

    return Response({"msg": "city updated successfuly!"})


@api_view(["DELETE"])
def delete_city(request: Request, city_id):
    try:
        city = City.objects.get(id=city_id)
        city.delete()
    except Exception as e:
        return Response({"msg": "city is not found!"})

    return Response({"msg": f"{city.name} city has been deleted!!"})


### Place Views

@api_view(["GET"])
def list_place(request: Request):
    places = Place.objects.all()
    places_data = PlaceSerializer(instance=places, many=True).data

    return Response({"msg": "list of all places", "places": places_data})


@api_view(['POST'])
def add_place(request: Request):
    place_serializer = PlaceSerializer(data=request.data)

    if place_serializer.is_valid():
        place_serializer.save()
    else: 
        return Response({"msg": "couldn't create place", "errors": place_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg": "place added successfuly!"}, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def update_place(request: Request, place_id):
    try:
        place = Place.objects.get(id=place_id)
    except Exception as e:
        return Response({"msg": "This place does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    place_serializer = PlaceSerializer(instance=place, data=request.data)

    if place_serializer.is_valid():
        place_serializer.save()
    else: 
        return Response({"msg": "couldn't update", "errors": place_serializer.errors})

    return Response({"msg": "place updated successfuly!"})


@api_view(["DELETE"])
def delete_place(request: Request, place_id):
    try:
        place = Place.objects.get(id=place_id)
        place.delete()
    except Exception as e:
        return Response({"msg": "place is not found!"})

    return Response({"msg": f"{place.name} has been deleted!!"})

