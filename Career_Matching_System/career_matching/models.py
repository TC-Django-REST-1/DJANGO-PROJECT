from operator import mod
from django.db import models

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=50)
    Address = models.TextField()


class Skill(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=40)
    jobs = models.ManyToManyField(Job)

class Skill_Job(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    
class Course(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()


