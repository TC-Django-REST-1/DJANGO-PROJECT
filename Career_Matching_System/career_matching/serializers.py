from dataclasses import fields
from pyexpat import model
from rest_framework import serializers

from .models import Job, Skill, Course, Skill_Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['name','type']

class SkillJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill_Job
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Course
        fields = '__all__'