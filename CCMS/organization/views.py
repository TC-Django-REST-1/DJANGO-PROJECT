from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Adminstration, Service, Employee,Company, Task,ManageRequset
from .serializers import AdminstrationSerializer,EmployeeSerializer,ServiceSerializer,RequsetSerializer,TaskSerializer,CompanySerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


#           ******************************** Adminstration ********************************

# Add new admin 
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def new_admin(request:Request):

    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"Message" : "Please Login!"},status=status.HTTP_401_UNAUTHORIZED)

    admin_serializer = AdminstrationSerializer(data=request.data)

    if admin_serializer.is_valid():
        admin_serializer.save()
    else:
        return Response({"Message" : "Couldn't Add Admin", "errors" : admin_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Admin created successfully"}, status=status.HTTP_201_CREATED)

# Get all Admins
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def read_admins(request:Request):

    #authenticated user info is stored in request.user
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login!"},status=status.HTTP_401_UNAUTHORIZED)

    #check if user not admin by search in admin list 
    all_admins = Adminstration.objects.all()
    print("User id",user.id)
    print("Username",user.username)
    
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to see adminstration info'
                }, status=status.HTTP_403_FORBIDDEN)

    admins_info = AdminstrationSerializer(instance=all_admins, many=True).data

    response_data = {
                "Message" : "All Admins List",
                "Admin" : admins_info
            }

    return Response(response_data, status=status.HTTP_200_OK)

# Update admin by id 
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_admin(request:Request,admin_id):
#check 
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login!"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        admin = Adminstration.objects.get(id = admin_id)
    except Exception as e:
        return Response({"Message" : "This admin is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to see adminstration info'
                }, status=status.HTTP_403_FORBIDDEN)
    
    admin_serializer = AdminstrationSerializer(instance=admin, data=request.data)

    if admin_serializer.is_valid():
        admin_serializer.save()
    else:
        return Response({"Message" : "Couldn't update", "errors" : admin_serializer.errors})

    return Response({"Message" : "Admin Information updated successfully"})


# Delete admin by id 
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_admin(request:Request,admin_id):
    
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login!"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        admin = Adminstration.objects.get(id = admin_id)
    except Exception as e:
        return Response({"Message" : "This admin is not found"}, status=status.HTTP_404_NOT_FOUND)
    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to see adminstration info'
                }, status=status.HTTP_403_FORBIDDEN)
    admin.delete()

    response_data = {
        "Message" : "Admin information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


#           ******************************** Services ********************************

# Add new service 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def new_service(request:Request):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to add service!'
                }, status=status.HTTP_403_FORBIDDEN)

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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_service(request:Request, service_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        service = Service.objects.get(id = service_id)
    except Exception as e:
        return Response({"Message" : "This service is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    service_serializer = ServiceSerializer(instance=service, data=request.data)

    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to update this service!'
                }, status=status.HTTP_403_FORBIDDEN)

    if service_serializer.is_valid():
        service_serializer.save()
    else:
        return Response({"Message" : "Couldn't update", "errors" : service_serializer.errors})

    return Response({"Message" : "Service updated successfully"})

# Delete service by id 
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_service(request:Request, service_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        service = Service.objects.get(id = service_id)
    except Exception as e:
        return Response({"Message" : "This service is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to delete this service!'
                }, status=status.HTTP_403_FORBIDDEN)
    service.delete()

    response_data = {
        "Message" : "Service information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


#           ******************************** Employees ********************************

# Add new Employee 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def new_employee(request:Request):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to add service!'
                }, status=status.HTTP_403_FORBIDDEN)

    employee_serializer = EmployeeSerializer(data=request.data)

    if employee_serializer.is_valid():
        employee_serializer.save()
    else:
        return Response({"Message" : "Couldn't Add Employee", "errors" : employee_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Employee added successfully"}, status=status.HTTP_201_CREATED)

# Get all Employees
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def read_employee(request:Request):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    all_admins = Adminstration.objects.all()
    all_employees = Employee.objects.all()

    if not any(user.username == x.username for x in all_admins) | any(user.email == x.email for x in all_employees):
    
        return Response({
            'Message': 'You do not have permission to see employee info!'
                }, status=status.HTTP_403_FORBIDDEN)
    print(user.id)
    employees_info = EmployeeSerializer(instance=all_employees, many=True).data

    response_data = {
        "Message" : "All Employees List",
        "Employees" : employees_info
    }

    return Response(response_data, status=status.HTTP_200_OK)

# Delete employee by id 
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_employee(request:Request, employee_id):
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        employee = Employee.objects.get(id = employee_id)
    except Exception as e:
        return Response({"Message" : "This employee is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to delete this employee!'
                }, status=status.HTTP_403_FORBIDDEN)
    employee.delete()

    response_data = {
        "Message" : "Employee information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)

# Edit Employee information.
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def edit_employee(request:Request,employee_id):
    
    user = request.user
    if not user.is_authenticated:
            return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        employee = Employee.objects.get(id = employee_id)
    except Exception as e:
        return Response({"Message" : "This employee is not found"}, status=status.HTTP_404_NOT_FOUND)

    employee_serializer = CompanySerializer(instance=employee, data=request.data)
    if user.id == employee.id:

        if employee_serializer.is_valid():
            employee_serializer.save()
        else:
            return Response({"Message" : "Couldn't update", "errors" : employee_serializer.errors})

    else:
        return Response({"Message" : "Only employee can update his profile"})
    return Response({"Message" : "Profile updated successfully"})



#           ******************************** Companies ********************************

# Add new company 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def new_company(request:Request):
    
    #check if user login
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)
    #if user login , take id and add it 
    company = Company(owner = user ,name = request.data["name"],
    email = request.data["email"], commercial_Id = request.data["commercial_Id"] ,
    mobile_number = request.data["mobile_number"],address = request.data["address"] )
  
    company.save()

    return Response({"Message" : "Company added successfully"}, status=status.HTTP_201_CREATED)


# Get all Companies
@authentication_classes([JWTAuthentication])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def read_companies(request:Request):
    
    user = request.user
    if not user.is_authenticated:
            return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    all_admins = Adminstration.objects.all()
    all_employees = Employee.objects.all()

    if not any(user.username == x.username for x in all_admins) | any(user.email == x.email for x in all_employees):
    
        return Response({
            'Message': 'You do not have permission to see employee info!'
                }, status=status.HTTP_403_FORBIDDEN)

    all_companies = Company.objects.all()
    for company in all_companies:
        print(company.owner.id)
        print(user.id)
        
    companies_info = CompanySerializer(instance=all_companies, many=True).data

    response_data = {
        "Message" : "All Companies List",
        "Companies" : companies_info
    }

    return Response(response_data, status=status.HTTP_200_OK)


# Get specific Companies
@authentication_classes([JWTAuthentication])
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def view_specific_companies(request:Request):
    
    user = request.user
    if not user.is_authenticated:
            return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    companies = Company.objects.filter(owner = user)
    company_data = CompanySerializer(instance=companies, many=True).data
    if len(company_data) == 0:
        response_data = {
        "Message" : "There is no any company",
    }
    else:
        response_data = {
            "Message" : "All Companies List",
            "Companies" : company_data
    }

    return Response(response_data, status=status.HTTP_200_OK)


# Delete company by id 
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_company(request:Request, company_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        company = Company.objects.get(id = company_id)
    except Exception as e:
        return Response({"Message" : "This company is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    all_admins = Adminstration.objects.all()
    if not any(user.username == x.username for x in all_admins):
        
        return Response({
            'Message': 'You do not have permission to delete this company!'
                }, status=status.HTTP_403_FORBIDDEN)
    
    company.delete()

    response_data = {
        "Message" : "Company information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)


# Edit Company information.
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def edit_companies(request:Request,company_id):
    
    user = request.user
    if not user.is_authenticated:
            return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        company = Company.objects.get(id = company_id)
    except Exception as e:
        return Response({"Message" : "This company is not found"}, status=status.HTTP_404_NOT_FOUND)

    company_serializer = CompanySerializer(instance=company, data=request.data)
    if user.id == company.owner.id:

        if company_serializer.is_valid():
            company_serializer.save()
        else:
            return Response({"Message" : "Couldn't update", "errors" : company_serializer.errors})

    else:
        return Response({"Message" : "Only owner of company can update"})
    return Response({"Message" : "Company updated successfully"})



#           ******************************** Requests ********************************

# Add new request 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def new_service_request(request:Request):

    #here in this function the goal is before create a request should check if service beneficiary_group for all users or spcifice
    
    #check if user login
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)
    
    service_request = RequsetSerializer(data=request.data)
    if service_request.is_valid():
            
        service_request.save()
    else:
        return Response({"Message" : "Couldn't make request ", "errors" : service_request.errors}, status=status.HTTP_403_FORBIDDEN)


    return Response({"Message" : "Request added successfully"}, status=status.HTTP_201_CREATED)


#Cancel requiest.
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_request(request:Request, request_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    try:
        req = ManageRequset.objects.get(id = request_id)
        print("hhhhh",req.id,user.id)
    except Exception as e:
        return Response({"Message" : "This request is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if user.id != req.user.id:
        return Response({
            'Message': 'You do not have permission to delete this request!'
                }, status=status.HTTP_403_FORBIDDEN)
    
    req.delete()

    response_data = {
        "Message" : "Request information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)
    

# Get my request
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_specific_request(request:Request):
    
    user = request.user
    if not user.is_authenticated:
            return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    req = ManageRequset.objects.filter(user = user)
    request_data = RequsetSerializer(instance=req, many=True).data
    if len(request_data) == 0:
        response_data = {
        "Message" : "There is no any request",
    }
    else:
        response_data = {
            "Message" : "All Companies List",
            "Companies" : request_data
    }

    return Response(response_data, status=status.HTTP_200_OK)


#           ******************************** Task ********************************

# Add new task 
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def new_task(request:Request):

    #here in this function the goal isassign request to employee
    
    #check if user login
    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)
    print(user.id)
    all_admins = Adminstration.objects.all()
    all_employees = Employee.objects.all()

    if not any(user.username == x.username for x in all_admins) | any(user.username == x.firstname for x in all_employees):
    
        return Response({
            'Message': 'You do not have permission to see tasks list!'
                }, status=status.HTTP_403_FORBIDDEN)

    task = TaskSerializer(data=request.data)
    if task.is_valid():
            
        task.save()
    else:
        return Response({"Message" : "Couldn't make request ", "errors" : task.errors}, status=status.HTTP_403_FORBIDDEN)


    return Response({"Message" : "Request added successfully"}, status=status.HTTP_201_CREATED)

#Cancel task.
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_task(request:Request, task_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)
   
    all_admins = Adminstration.objects.all()
    all_employees = Employee.objects.all()
    try:
        task = Task.objects.get(id = task_id)
    except Exception as e:
        return Response({"Message" : "This task is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if not any(user.username == x.username for x in all_admins) | any(user.username == x.firstname for x in all_employees):
        
        return Response({
            'Message': 'You do not have permission to see tasks list!'
                }, status=status.HTTP_403_FORBIDDEN)
    
    task.delete()

    response_data = {
        "Message" : "Request information deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)
    


# Search  service
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def search_service(request:Request,name:str):
    
    user = request.user
    if not user.is_authenticated:
            return Response({"Message" : "Please Login"},status=status.HTTP_401_UNAUTHORIZED)

    sc = Service.objects.filter(name = name)
    service_data = ServiceSerializer(instance=sc, many=True).data

    response_data = {
            "Service" : service_data
    }
    return Response(response_data, status=status.HTTP_200_OK)



