from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .serializers import BranchSerializer
from .serializers import CarSerializer
from .serializers import reservedCarSerializer

from .models import Branch
from .models import Car
from .models import reservedCar


# Branch Section 

@api_view(['POST'])
def create_Branch(request : Request):

    Branch_serializer = BranchSerializer(data=request.data)

    if Branch_serializer.is_valid():
        Branch_serializer.save()
    else:
        return Response({"msg" : "couldn't create a Branch", "errors" : Branch_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "Branch Added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_Branchs(request : Request):
    try:
        if "branch_id" in request.query_params:
            branch=Branch.objects.get(id=request.query_params["branch_id"])
            branchs_data = BranchSerializer(instance=branch).data
        else:
            branch=Branch.objects.all()
            branchs_data = BranchSerializer(instance=branch, many=True).data
    except Exception as e:
            return Response({"msg" : "This branch is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "list of all Branchs", "Branchs" : branchs_data})


@api_view(['PUT'])
def update_Branch(request : Request, branch_id):

    try:
        branch = Branch.objects.get(id=branch_id)
    except Exception as e:
        return Response({"msg" : "This branch is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    branch_serializer = BranchSerializer(instance=branch, data=request.data)

    if branch_serializer.is_valid():
        branch_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : branch_serializer.errors})

    return Response({"msg" : "Branch updated successfully"})


@api_view(['DELETE'])
def delete_Branch(request : Request, branch_id):

    try:
        branch = Branch.objects.get(id=branch_id)
        branch.delete()
    except Exception as e:
        return Response({"msg" : "This Branch is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "Branch Deleted successfully"})


# Car Section 

@api_view(['POST'])
def create_car(request : Request):

    car_serializer = CarSerializer(data=request.data)

    if car_serializer.is_valid():
        car_serializer.save()
    else:
        return Response({"msg" : "couldn't create a Car", "errors" : car_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "Car Added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_car(request : Request):
    
    try:
        if "branch_id" in request.query_params:
            car=Car.objects.filter(branch_id=request.query_params["branch_id"])
            cars_data = CarSerializer(instance=car,  many=True).data
        elif "car_id" in request.query_params:
            car=Car.objects.get(id=request.query_params["car_id"])
            cars_data = CarSerializer(instance=car).data
        else:
            car=Car.objects.all()
            cars_data = CarSerializer(instance=car,  many=True).data

    except Exception as e:
        return Response({"msg" : "This branch is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "list of all Cars", "Cars" : cars_data})


@api_view(['PUT'])
def update_car(request : Request, car_id):

    try:
        car = Car.objects.get(id=car_id)
    except Exception as e:
        return Response({"msg" : "This car is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    car_serializer = CarSerializer(instance=car, data=request.data)

    if car_serializer.is_valid():
        car_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : car_serializer.errors})

    return Response({"msg" : "Car updated successfully"})


@api_view(['DELETE'])
def delete_car(request : Request, car_id):

    try:
        car = Car.objects.get(id=car_id)
        car.delete()
    except Exception as e:
        return Response({"msg" : "This car is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "Car Deleted successfully"})


# Car Reserved Section 

@api_view(['POST'])
def create_reservedCar(request : Request):

    reservedCar_serializer = reservedCarSerializer(data=request.data)
    car=Car.objects.get(request.data["car_id"])

    if reservedCar_serializer.is_valid():
        if not car.is_available:
            reservedCar_serializer.save()
            car.is_available=False
            Car_serializer= CarSerializer(data=car)
            Car_serializer.save()
        else:
            return Response({"msg" : "Car is not vailable, couldn't reserve the car", "errors" : reservedCar_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    else:
        return Response({"msg" : "couldn't reserve the car", "errors" : reservedCar_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "The Car reserved Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_reservedCar(request : Request):
    if "user_id" in request.query_params:
        cars=reservedCar.objects.get(user=request.query_params["user_id"])
    else:
        cars=reservedCar.objects.all()

    reservedCar_data = reservedCarSerializer(instance=cars).data
    return Response({"msg" : "list of all reserved Cars", "Cars" : reservedCar_data})


@api_view(['PUT'])
def update_reservedCar(request : Request, car_id):

    try:
        car = reservedCar.objects.get(id=car_id)
    except Exception as e:
        return Response({"msg" : "This car is not found in the list of reseved cars"}, status=status.HTTP_404_NOT_FOUND)
    
    reservedCar_serializer = reservedCarSerializer(instance=car, data=request.data)

    if reservedCar_serializer.is_valid():
        reservedCar_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : reservedCar_serializer.errors})

    return Response({"msg" : "Car updated successfully"})


@api_view(['DELETE'])
def delete_reservedCar(request : Request, car_id):

    try:
        Deletedcar = reservedCar.objects.get(id=car_id)
        Deletedcar.delete()
        car=Car.objects.get(request.data["car_id"])
        car.is_available=True
        Car_serializer= CarSerializer(data=car)
        Car_serializer.save()
    except Exception as e:
        return Response({"msg" : "This car is not found in the list of reserved Cars"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "Car Deleted successfully"})
    
