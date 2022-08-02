import imp
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from.models import Restaurants, Meals
from .serializer import RestaurantsSerializer, MealsSerializer



@api_view(['POST'])
def add_restaurant(request : Request):
    
    restaurant_serializer = RestaurantsSerializer(data= request.data)
    if restaurant_serializer.is_valid():
        restaurant_serializer.save()
    else:
        return Response({"msg" : "couldn't create a retaurants", "errors" : restaurant_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({"msg" : "The restaurants Added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_restaurants(request : Request):
    
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        restaurants = Restaurants.objects.filter(title=search_phrase)[skip:get]
    else:
        restaurants = Restaurants.objects.all()
        
    restaurant_data = RestaurantsSerializer(instance=restaurants, many=True).data

    return Response({"msg" : "list of all restaurants", "restaurants" : restaurant_data})



@api_view(['PUT'])
def update_restaurant(request : Request, restaurant_id):

    try:
        restaurant = Restaurants.objects.get(id = restaurant_id)
    except Exception as e:
        return Response({"msg" : "This restaurant is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    restaurant_serializer = RestaurantsSerializer(instance=restaurant, data=request.data)

    if restaurant_serializer.is_valid():
        restaurant_serializer.save()
    else:
        return Response({"msg" : "couldn't update this restaurant", "errors" : restaurant_serializer.errors})

    return Response({"msg" : "The restaurant updated successfully"})



@api_view(["DELETE"])
def delete_restaurant(request : Request, restaurant_id):

    try:
        restaurant = Restaurants.objects.get(id = restaurant_id)
        restaurant.delete()
    except Exception as e:
        return Response({"msg" : "The restaurant is not Found!"})

    return Response({"msg" : f"delete the following restaurant {restaurant.restaurant_name}"})


#meals



@api_view(['POST'])
def add_meal(request : Request):
    
    meal_serializer = MealsSerializer(data= request.data)
    if meal_serializer.is_valid():
        meal_serializer.save()
    else:
        return Response({"msg" : "couldn't create a meal", "errors" : meal_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({"msg" : "The meal Added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_meals(request : Request):
    
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        meals = Meals.objects.filter(title=search_phrase)[skip:get]
    else:
        meals = Meals.objects.all()
        
    meals_data = MealsSerializer(instance=meals, many=True).data

    return Response({"msg" : "list of all meals", "meals" : meals_data})


@api_view(['PUT'])
def update_meal(request : Request, meal_id):

    try:
        meal = Meals.objects.get(id = meal_id)
    except Exception as e:
        return Response({"msg" : "This meal is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    meal_serializer = MealsSerializer(instance=meal, data=request.data)

    if meal_serializer.is_valid():
        meal_serializer.save()
    else:
        return Response({"msg" : "couldn't update this meal", "errors" : meal_serializer.errors})

    return Response({"msg" : "The meal updated successfully"})



@api_view(["DELETE"])
def delete_meal(request : Request, meal_id):

    try:
        meal = Meals.objects.get(id = meal_id)
        meal.delete()
    except Exception as e:
        return Response({"msg" : "The meal is not Found!"})

    return Response({"msg" : f"delete the following meal {meal.name}"})