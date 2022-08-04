from dataclasses import Field, fields
from pyexpat import model
from rest_framework import serializers

from .models import  movie_schedule, movies_info, user_ticket, movies_feedback

class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model = movies_info
        fields ='__all__'

class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = movie_schedule
        fields = '__all__'

class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = user_ticket
        fields = '__all__'

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta:
        model = movies_feedback
        fields = '__all__'
