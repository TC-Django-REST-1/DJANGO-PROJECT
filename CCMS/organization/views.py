from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Adminstration, Service, Employee,Company
from users.models import Consumer
from .serializers import AdminstrationSerializer,EmployeeSerializer,ServiceSerializer,RequsetSerializer,TaskSerializer,CompanySerializer
from users.serializers import ConsumerSerializer


#           ******************************** Adminstration ********************************

# Add new admin 
@api_view(['POST'])
def new_admin(request:Request):

    admin_serializer = AdminstrationSerializer(data=request.data)

    if admin_serializer.is_valid():
        admin_serializer.save()
    else:
        return Response({"Message" : "Couldn't Add Admin", "errors" : admin_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Admin created successfully"}, status=status.HTTP_201_CREATED)

# Get all Admins
@api_view(['GET'])
def read_admins(request:Request):

    all_admins = Adminstration.objects.all()
    admins_info = AdminstrationSerializer(instance=all_admins, many=True).data

    response_data = {
        "Message" : "All Admins List",
        "Admin" : admins_info
    }

    return Response(response_data, status=status.HTTP_200_OK)


# Update admin by id 
@api_view(['PUT'])
def update_admin(request:Request,admin_id):

    try:
        admin = Adminstration.objects.get(id = admin_id)
    except Exception as e:
        return Response({"Message" : "This admin is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    admin_serializer = AdminstrationSerializer(instance=admin, data=request.data)

    if admin_serializer.is_valid():
        admin_serializer.save()
    else:
        return Response({"Message" : "Couldn't update", "errors" : admin_serializer.errors})

    return Response({"Message" : "Admin Information updated successfully"})


# Delete admin by id 
@api_view(['DELETE'])
def delete_admin(request:Request,admin_id):
    
    try:
        admin = Adminstration.objects.get(id = admin_id)
    except Exception as e:
        return Response({"Message" : "This admin is not found"}, status=status.HTTP_404_NOT_FOUND)
    admin.delete()

    response_data = {
        "Message" : "Admin information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


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
        "Services" : service_data
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
    try:
        service = Service.objects.get(id = service_id)
    except Exception as e:
        return Response({"Message" : "This service is not found"}, status=status.HTTP_404_NOT_FOUND)
    service.delete()

    response_data = {
        "Message" : "Service information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


#           ******************************** Employees ********************************

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
        "Employees" : employees_info
    }

    return Response(response_data, status=status.HTTP_200_OK)

# Delete employee by id 
@api_view(['DELETE'])
def delete_employee(request:Request, employee_id):

    try:
        employee = Employee.objects.get(id = employee_id)
    except Exception as e:
        return Response({"Message" : "This employee is not found"}, status=status.HTTP_404_NOT_FOUND)
    employee.delete()

    response_data = {
        "Message" : "Employee information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


#           ******************************** Companies ********************************

# Add new Company 
@api_view(['POST'])
def new_company(request:Request):

    company_serializer = CompanySerializer(data=request.data)

    if company_serializer.is_valid():
        company_serializer.save()
    else:
        return Response({"Message" : "Couldn't Add Company", "errors" : company_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Company added successfully"}, status=status.HTTP_201_CREATED)

# Get all Companies
@api_view(['GET'])
def read_companies(request:Request):

    all_companies = Company.objects.all()
    companies_info = CompanySerializer(instance=all_companies, many=True).data

    response_data = {
        "Message" : "All Companies List",
        "Companies" : companies_info
    }

    return Response(response_data, status=status.HTTP_200_OK)

# Delete company by id 
@api_view(['DELETE'])
def delete_company(request:Request, company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Exception as e:
        return Response({"Message" : "This company is not found"}, status=status.HTTP_404_NOT_FOUND)

    company.delete()

    response_data = {
        "Message" : "Company information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)
    