from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Adminstration OR orgnization
class Adminstration(models.Model):
    username = models.CharField(max_length=512)
    email = models.EmailField(max_length=512)
    password = models.CharField(max_length=512)


class Employee(models.Model):
    admin = models.ForeignKey(Adminstration, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    Birthdate = models.DateField()
    password = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=128)
    Department = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=6, decimal_places=2)


class Service(models.Model):
    admin = models.ForeignKey(Adminstration, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    service_duration = models.CharField(max_length=128)
    beneficiary_group = models.CharField(max_length=128)
    Fees = models.IntegerField()
    service_steps = models.TextField()

class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    email = models.EmailField()
    commercial_Id = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

# class requset 
class ManageRequset(models.Model):
    service  = models.ForeignKey(Service, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)# defult value timezone


class Task(models.Model):
    service  = models.ForeignKey(Service, on_delete=models.CASCADE)
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company =  models.ForeignKey(Company, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True)# defult value timezone