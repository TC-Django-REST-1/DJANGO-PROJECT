from rest_framework import serializers

from .models import Adminstration,Employee,Company,Service,ManageRequset,Task


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
        fields = ['name','email','mobile_number','address']

class RequsetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ManageRequset
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'