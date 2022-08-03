from nis import cat
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status

from .models import Company, Job
from .serializers import JobSerializer
from django.contrib.auth.models import User


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_company(request : Request):

    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('companies.add_company'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    name = request.data["name"]
    permit_number = request.data["permit_number"]
    owner = request.user
    category = request.data["category"]
    no_of_pilgrims = request.data["no_of_pilgrims"]
    location_url = request.data["location_url"]

    if category not in ['Abraj','A','B','C','D','E']:
        return Response({"msg" : f"{category} is wrong category."}, status=status.HTTP_401_UNAUTHORIZED)

    new_company = Company(name=name, permit_number=permit_number, owner=owner, category=category, no_of_pilgrims=no_of_pilgrims, location_url=location_url)
    new_company.save()

    res_data = {
        "msg" : "Created Company Successfully"
    }

    return Response(res_data)



@api_view(["GET"])
def list_companies(request : Request):

    all_companies = Company.objects.all().order_by('-category')
    all_companies_list = [{"id" : company.id, "name":company.name, "permit_number": company.permit_number, "owner": company.owner.username, "category": company.category, "no_of_pilgrims": company.no_of_pilgrims, "location_url": company.location_url} for company in all_companies]
    
    res_data = {
        "msg" : "A list of All Companies",
        "companies" : all_companies_list
    }

    return Response(res_data, status=status.HTTP_200_OK)



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_company(request : Request, company_id):

    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('companies.change_company'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.data['category'] not in ['Abraj','A','B','C','D','E']:
        return Response({"msg" : f"{request.data['category']} is wrong category."}, status=status.HTTP_401_UNAUTHORIZED)


    company = Company.objects.get(id=company_id)     
    company.name = request.data["name"]
    company.permit_number = request.data["permit_number"]
    company.category = request.data["category"]
    company.no_of_pilgrims = request.data["no_of_pilgrims"]
    company.location_url = request.data["location_url"]

    company.save()

    return Response({"msg" : "Your comany is updated !"})



@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_company(request : Request, company_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    if not user.has_perm('companies.delete_company'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        company = Company.objects.get(id=company_id)
        company.delete()
    except Exception as e:
        return Response({"msg" : "The company is not Found!"})

    return Response({"msg" : f"delete the following company {company.name}"})



@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_job(request : Request):

    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    if not user.has_perm('companies.add_job'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    company_owner = request.user
    company = Company.objects.get(owner=company_owner)
    
    request.data["company"] = company.id
    request.data["applicants"] = []

    print(">>>>", request.data["company"])
    print(">>>>", request.data["applicants"])

    job_serializer = JobSerializer(data=request.data)

    if job_serializer.is_valid():
        job_serializer.save()
    else:
        return Response({"msg" : "couldn't create a job", "errors" : job_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Job Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_jobs(request : Request):

    jobs = Job.objects.all()
    jobs_data = JobSerializer(instance=jobs, many=True).data

    return Response({"msg" : "list of all jobs", "jobs" : jobs_data})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_job(request : Request, job_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    if not user.has_perm('companies.change_job'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        job = Job.objects.get(id=job_id)
    except Exception as e:
        return Response({"msg" : "This job is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    job_serializer = JobSerializer(instance=job, data=request.data)

    if job_serializer.is_valid():
        job_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : job_serializer.errors})

    return Response({"msg" : "Job updated successfully"})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_job(request : Request, job_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    if not user.has_perm('companies.delete_job'):
        return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        job = Job.objects.get(id=job_id)
        job.delete()
    except Exception as e:
        return Response({"msg" : "This job is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : f"delete the following company {job.title}"})



@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def apply_to_job(request : Request, job_id):

    user = request.user
    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    if user.has_perm('companies.add_company'):
        return Response({"msg" : "Companies don't have applying to jobs permission!"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        desired_job = Job.objects.get(id=job_id)
        
        if desired_job.employee is not None:
            return Response({"msg" : "This job is no longer available! Try to apply to another job."}, status=status.HTTP_404_NOT_FOUND)

        desired_job.applicants.add(request.user)
        desired_job.save()


    except Exception as e:
        return Response({"msg" : "This job is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : f"You applied to {desired_job.title} at {desired_job.company.name} successfully."})
    


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def appointing_employee(request : Request, job_id, applicant_id):

    owner = request.user
    if not owner.is_authenticated:
        return Response({"msg" : "Please Log In"})
    # if not owner.has_perm('companies.add_company'):
    #     return Response({"msg" : "You don't have permission ! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        applicant = User.objects.get(id=applicant_id)
    except Exception as e:
        return Response({"msg" : "This applicant is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        job = Job.objects.get(id=job_id)
        if applicant not in job.applicants.all():
            return Response({"msg" : f"{applicant.username} didn't apply for this job!"}, status=status.HTTP_404_NOT_FOUND)
        if job.employee is not None:
            return Response({"msg" : f"This job is appointed to {job.employee.username}!"}, status=status.HTTP_404_NOT_FOUND)  
        job.employee = applicant
        job.save()
    except Exception as e:
        return Response({"msg" : "This job is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : f"{job.title} appointed to {applicant.username} successfully."})
    




