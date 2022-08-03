from rest_framework import serializers

from .models import Adminstration,Employee,Company,Service,Requset,Task


class AdminstrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adminstration
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'

class RequsetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Requset
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'