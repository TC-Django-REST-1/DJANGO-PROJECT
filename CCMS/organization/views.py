from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Service, Employee
from .serializers import AdminstrationSerializer,EmployeeSerializer,ServiceSerializer,RequsetSerializer,TaskSerializer


#           ******************************** Services ********************************

# Add new service 
@api_view(['POST'])
def new_service(request:Request):

    service_serializer = ServiceSerializer(data=request.data)

    if service_serializer.is_valid():
        service_serializer.save()
    else:
        return Response({"Message" : "Couldn't create a service", "errors" : service_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Service added successfully"}, status=status.HTTP_201_CREATED)

# Get all services
@api_view(['GET'])
def read_service(request:Request):

    all_services = Service.objects.all()
    service_data = ServiceSerializer(instance=all_services, many=True).data

    response_data = {
        "Message" : "All Services List",
        "Brand" : service_data
    }

    return Response(response_data, status=status.HTTP_200_OK)


# Update service by id 
@api_view(['PUT'])
def update_service(request:Request, service_id):

    try:
        service = Service.objects.get(id = service_id)
    except Exception as e:
        return Response({"Message" : "This service is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    service_serializer = ServiceSerializer(instance=service, data=request.data)

    if service_serializer.is_valid():
        service_serializer.save()
    else:
        return Response({"Message" : "Couldn't update", "errors" : service_serializer.errors})

    return Response({"Message" : "Service updated successfully"})

# Delete service by id 
@api_view(['DELETE'])
def delete_service(request:Request, service_id):
    
    service = Service.objects.get(id = service_id)
    service.delete()

    response_data = {
        "Message" : "Service information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


#           ******************************** Employee ********************************

# Add new Employee 
@api_view(['POST'])
def new_employee(request:Request):

    employee_serializer = EmployeeSerializer(data=request.data)

    if employee_serializer.is_valid():
        employee_serializer.save()
    else:
        return Response({"Message" : "Couldn't Add Employee", "errors" : employee_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Employee added successfully"}, status=status.HTTP_201_CREATED)

# Get all Employees
@api_view(['GET'])
def read_employee(request:Request):

    all_employees = Employee.objects.all()
    employees_info = EmployeeSerializer(instance=all_employees, many=True).data

    response_data = {
        "Message" : "All Employees List",
        "Brand" : employees_info
    }

    return Response(response_data, status=status.HTTP_200_OK)

# Delete employee by id 
@api_view(['DELETE'])
def delete_employee(request:Request, employee_id):
    
    service = Employee.objects.get(id = employee_id)
    service.delete()

    response_data = {
        "Message" : "Employee information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)
    