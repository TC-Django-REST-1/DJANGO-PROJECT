from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import status

from .models import Brand
# , Car
from .serializers import BrandSerilizer
# ,CarSerilizer


# BrandSerilizer
@api_view(['POST'])
def add_brand(request: Request):
    new_brand_serializer = BrandSerilizer(data=request.data)
    if new_brand_serializer.is_valid():
        new_brand_serializer.save()
    else:
        return Response({"msg" : "couldn't add a new brand", "errors" : new_brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "A new brand added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def brand_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        brands = Brand.objects.filter(brand__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        brands = Brand.objects.order_by("-id").all()[skip:get]

    data = BrandSerilizer(brands, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id = brand_id)
        data = BrandSerilizer(instance=brand, data=request.data)
        if data.is_valid():
            data.save()
            return Response({"msg" : "Brand updated successfully "}, status=status.HTTP_200_OK)
        else:
            return Response({"msg" : "couldn't update the brand", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"msg" : f"The brand with ID No:{brand_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id = brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : f"The brand with ID No:{brand_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"A brand with ID No:{brand_id} has been deleted successfully"}, status=status.HTTP_200_OK)




# # CarSerilizer
# @api_view(['POST'])
# def add_car(request: Request):
#     new_car_serilizer = CarSerilizer(data=request.data)
#     if new_car_serilizer.is_valid():
#         new_car_serilizer.save()
#     else:
#         return Response({"msg" : "couldn't add a new car", "errors" : new_car_serilizer.errors}, status=status.HTTP_403_FORBIDDEN)

#     return Response({"msg" : "A new car created successfully"}, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def cars_list(request: Request):

#     skip = int(request.query_params.get("skip", 1))
#     get = int(request.query_params.get("get", 4))


#     cars = Car.objects.order_by("-id").all()[skip:get]
#     data = CarSerilizer(cars, many=True).data
#     return Response(data, status=status.HTTP_200_OK)

# @api_view(['PUT'])
# def update_car(request: Request, car_id):
#     car = Car.objects.get(id = car_id)
#     data = CarSerilizer(instance=car, data=request.data)
#     if data.is_valid():
#         data.save()
#         return Response({"msg" : "Car updated successfully "}, status=status.HTTP_200_OK)
#     else:
#         return Response({"msg" : "couldn't update the car", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def remove_car(request: Request, car_id):
#     try:
#         car = Car.objects.get(id = car_id)
#         car.delete()
#     except Exception as e:
#         return Response({"msg" : f"The car with ID No:{car_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

#     return Response({"msg" : f"A car with ID No:{car_id} has been deleted successfully"}, status=status.HTTP_200_OK)




# @api_view(['GET'])
# def brand_cars_list(request: Request, brand_name):
#     try:
#         brand = Brand.objects.get(name = brand_name) # get the whole info of brand by its brand_name so we can extract the id of that brand
#         cars = Car.objects.filter(brand__exact=brand.id) # filter all products by the brand.id because the Product model has only the id of the brand not the name
#         data = CarSerilizer(cars, many=True).data
#         return Response(data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"msg" : f"The brand with ID No:{brand_name} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)