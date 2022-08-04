from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobSerializer, SkillSerializer, SkillJobSerializer, CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Job, Skill, Course, Skill_Job

# Create your views here.

# -------------------------------- Job CRUD Proccesses -------------------- #

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_job(request: Request):
    

    job_serializer = JobSerializer(data=request.data)

    if job_serializer.is_valid():
        job_serializer.save()
    else:
        return Response({'message' : 'Could not add a job', 'Errors' : JobSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({'message' : 'Job Added successfully!'}, status=status.HTTP_201_CREATED) 


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_job(request: Request):
    
    skip = int(request.query_params.get('skip', 0))
    get = int(request.query_params.get('get', 3))

    jobs = Job.objects.all()
    jobs_serializer = JobSerializer(instance=jobs, many=True).data[skip:get]
    

    return Response({'message' : 'List of Jobs ', 'Jobs' : jobs_serializer}, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def update_job(request: Request, job_id):
    
    try:
       job = Job.objects.get(id=job_id)
    except Exception as e:
        return Response({'message' : 'No job found for thi id!'}, status=status.HTTP_404_NOT_FOUND)

    job_updated = JobSerializer(instance=job, data=request.data)

    if job_updated.is_valid():
        job_updated.save()
    else:
        return Response({'message' : 'Could not update job data!', 'Errors' : JobSerializer.errors},status=status.HTTP_403_FORBIDDEN)
    
    return Response({'message' : 'Job data updated Successfully!'}, status=status.HTTP_202_ACCEPTED)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def delete_job(request: Request, job_id):
   
    try:
        job = Job.objects.get(id=job_id)
        job.delete()
    except Exception as e:
        return Response({'message' : 'No job found with tis id'}, status=status.HTTP_404_NOT_FOUND)


    return Response({'message' : 'Job deleted successfylly!'}, status=status.HTTP_200_OK)


# -------------------------------- Skill CRUD Proccesses -------------------- #

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_skill(request: Request):
    
    skill_serializer = SkillSerializer(data=request.data)

    if skill_serializer.is_valid():
        skill_serializer.save()
    else:
        return Response({'message' : 'could not add a skill!', 'Error' : SkillSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({'message' : 'Skill Added successfully!'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_skill(request: Request):

    #search = request.query_params['search']

    skills = Skill.objects.all()#.filter(name__contains=search)
    skills_serializer = SkillSerializer(instance=skills, many=True).data

    return Response({'message' : 'List of skills' , 'Skills' : skills_serializer}, status=status.HTTP_200_OK)

   
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def update_skill(request: Request, skill_id):
    
    try:
       skill = Skill.objects.get(id=skill_id)
    except Exception as e:
        return Response({'message' : 'Could not add skill!'}, status=status.HTTP_404_NOT_FOUND)
    
    skill_updated = SkillSerializer(instance=skill, data=request.data)

    if skill_updated.is_valid():
        skill_updated.save()
    else:
        return Response({'message' : 'Could not update skill!', 'Error' : SkillSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({'message' : 'Skill updated successfully!'}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_job_skill(request: Request):
    
    skill_job = SkillJobSerializer(data=request.data)

    if skill_job.is_valid():
        skill_job.save()
    else:
        return Response({'message' : 'Could not add ids for skill and job!', 'Error' : SkillJobSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({'message' : 'Skill_Job ids added successfully!'}, status=status.HTTP_201_CREATED)


# -------------------------------- Course CRUD Proccesses -------------------- #

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_course(request: Request):
    
    course_serializer = CourseSerializer(data=request.data)

    if course_serializer.is_valid():
        course_serializer.save()
    else:
        return Response({'message' : 'Could not add course', 'Error' : CourseSerializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({'message' : 'course added successfully!'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_course(request: Request):
    
    
    courses = Course.objects.all()
    courses_serializer = CourseSerializer(instance=courses, many=True).data

    return Response({'List of courses' : courses_serializer }, status=status.HTTP_200_OK)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def update_course(request: Request, course_id):
    
    try:
        course = Course.objects.get(id=course_id)
    except Exception as e:
        return Response({'message' : 'Not found a course!'}, status=status.HTTP_404_NOT_FOUND)

    course_updated = CourseSerializer(instance=course, data=request.data)

    if course_updated.is_valid():
        course_updated.save()
    else:
        return Response({'message' : 'Could not update course data', 'Error' : CourseSerializer.errors},status=status.HTTP_403_FORBIDDEN)

    return Response({'message' : 'Course updated successfully!'}, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def delete_course(request: Request, course_id):
    
    try:
        course = Course.objects.get(id=course_id)
        course.delete()
    except Exception as e:
        return Response({'message' : 'Not found a course!'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message' : 'Course deleted successfully!'}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_skills_courses_of_job(request: Request):
    
    if 'search_id' in request.query_params:
        search_id = int(request.query_params.get('search_id'))
        all_courses = Course.objects.filter(job_id=search_id)
        #all_skills = Skill_Job.objects.filter(id=search_id)
    else:
        all_courses = Course.objects.all()

    courses = CourseSerializer(instance=all_courses, many=True).data
    #skills = SkillSerializer(instance=all_skills, many=True).data

    return Response({'message' : 'List of job skills and courses required:', 'courses' : courses})