from django.db import models
from users.models import Cpmpany

# Create your models here.
#Adminstration OR orgnization
class Adminstration(models.Model):
    username = models.CharField(max_length=512)
    email = models.EmailField(max_length=512)
    password = models.CharField(max_length=512)


class Employee(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    Birthdate = models.DateField()
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=128)
    Department = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=6, decimal_places=2)



class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    service_duration = models.CharField(max_length=128)
    beneficiary_group = models.CharField(max_length=128)
    Fees = models.IntegerField()
    service_steps = models.TextField()

# class requset 
# requiset must be from comapny 
class Requset(models.Model):
    service  = models.ForeignKey(Service, on_delete=models.CASCADE)
    company =  models.ForeignKey(Cpmpany, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)# defult value timezone


class Task(models.Model):
    service  = models.ForeignKey(Service, on_delete=models.CASCADE)
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company =  models.ForeignKey(Cpmpany, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)# defult value timezone