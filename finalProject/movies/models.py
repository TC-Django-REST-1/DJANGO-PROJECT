from pydoc import describe
from django.db import models

# Create your models here.

    
class movies_info (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    release_at = models.DateField()
    genres = models.CharField(max_length=200)


class movie_schedule (models.Model): 
    movie = models.ForeignKey(movies_info,on_delete=models.CASCADE)
    total_seats = models.IntegerField()
    location = models.CharField(max_length=200)
    movie_date =  models.DateField()
    showtime = models.TimeField()
    subtitle = models.CharField(max_length=200)
    screen = models.IntegerField()


class user_ticket (models.Model):
    schedule_id = models.ForeignKey(movie_schedule,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2,)
    reservtion_code = models.CharField(max_length=10)
    ticket_class = models.CharField(max_length=50)
    seat = models.CharField(max_length=4)
