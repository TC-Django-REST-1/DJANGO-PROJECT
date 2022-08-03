from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User



class Company(models.Model):
    name = models.CharField(max_length=512)
    permit_number = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = [('Abraj', 'Abraj'),('A','A'),('B','B'),('C','C'),('D','D'),('E','E')]
    category = models.CharField(max_length=8, choices=CHOICES)
    no_of_pilgrims = models.IntegerField()
    location_url = models.URLField()

    def __str__(self) -> str:
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=512)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    required_skills = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    applicants = models.ManyToManyField(User, blank=True, related_name='applicants')

    def __str__(self) -> str:
        return self.company.name + ' - ' + self.title