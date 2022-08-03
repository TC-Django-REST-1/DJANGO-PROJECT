from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import movie_schedule, movies_info, user_ticket
from .serializers import  MoviesSerializers, ScheduleSerializers, TicketSerializers
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

# Post new movie
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_movie(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    movies_serializers = MoviesSerializers(data=request.data)
    if movies_serializers.is_valid():
        movies_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new movie", "errors":movies_serializers.errors})
    return Response({"msg" : "Movie Added Successfully"})

# List all movies
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_movie(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
            
  #  skip = int(request.query_params.get("skip",0))
  #  get  = int(request.query_params.get("get",10))
   # search_p = request.query_params["search"]

   # movie = movies_info.objects.all().filter(title=search_p)[skip:get]
    movie = movies_info.objects.all()
    movie_data = MoviesSerializers(instance=movie, many=True).data

    return Response({"msg" : "List of all Movies", "Movie " : movie_data})

# Update movie
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
def update_movie(request : Request, movie_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    try:
        movie = movies_info.objects.get(id=movie_id)
    except Exception as e:
        return Response({"msg" : "This movie is not found"})

    movie_Serializer = MoviesSerializers(instance=movie, data=request.data)

    if movie_Serializer.is_valid():
        movie_Serializer.save()
        return Response({"msg" : "Movie is updated"})
    else:
        return Response({"msg" : "Couldn't update movie"})

# Delete Movie
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
def delete_movie(request : Request, movie_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    try:
        movie = movies_info.objects.get(id=movie_id)
        msg = f"delete the following movie {movie.name}"
        movie.delete()
    except Exception as e:
        return Response({"msg" : "The movie is not found "})
    return Response({"msg":msg})
    
# Post new Schedule
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_schedule(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    Schedule_serializers = ScheduleSerializers(data=request.data)
    if Schedule_serializers.is_valid():
        Schedule_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new Schedule", "errors":Schedule_serializers.errors})
    return Response({"msg" : "Schedule Added Successfully"})

# List all Schedule
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_schedule(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    
  #  skip = int(request.query_params.get("skip",0))
  #  get  = int(request.query_params.get("get",10))
   # search_p = request.query_params["search"]

   # movie = movies_info.objects.all().filter(title=search_p)[skip:get]
    Schedule = movie_schedule.objects.all()
    Schedule_data = ScheduleSerializers(instance=Schedule, many=True).data

    return Response({"msg" : "List of all Schedule", "Schedule " : Schedule_data})

# Update Schedule
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
def update_schedule(request : Request, schedule_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    try:
        schedule = movie_schedule.objects.get(id=schedule_id)
    except Exception as e:
        return Response({"msg" : "This schedule is not found"})

    schedule_Serializer = ScheduleSerializers(instance=schedule, data=request.data)

    if schedule_Serializer.is_valid():
        schedule_Serializer.save()
        return Response({"msg" : "Schedule is updated"})
    else:
        return Response({"msg" : "Couldn't update schedule"})

# Delete Schedule
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
def delete_schedule(request : Request, schedule_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    try:
        schedule = movie_schedule.objects.get(id=schedule_id)
        msg = f"delete the following director {schedule.id}"
        schedule.delete()
    except Exception as e:
        return Response({"msg" : "The schedule is not found "})
    return Response({"msg":msg})
    
# Post new Ticket
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_ticket(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})
    ticket_serializers = TicketSerializers(data=request.data)
    if ticket_serializers.is_valid():
        ticket_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new ticket", "errors":ticket_serializers.errors})
    return Response({"msg" : "Your ticket Added Successfully"})

# List all tickets
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_ticket(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})   
  #  skip = int(request.query_params.get("skip",0))
  #  get  = int(request.query_params.get("get",10))
   # search_p = request.query_params["search"]

   # movie = movies_info.objects.all().filter(title=search_p)[skip:get]
    ticket = user_ticket.objects.all()
    ticket_data = TicketSerializers(instance=ticket, many=True).data

    return Response({"msg" : "List of all Users Ticket", "User Ticket " : ticket_data})

# Update Ticket
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
def update_ticket(request : Request, ticket_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})  
    try:
        ticket = user_ticket.objects.get(id=ticket_id)
    except Exception as e:
        return Response({"msg" : "This ticket is not found"})

    ticket_Serializer = TicketSerializers(instance=ticket, data=request.data)

    if ticket_Serializer.is_valid():
        ticket_Serializer.save()
        return Response({"msg" : "Ticket is updated"})
    else:
        return Response({"msg" : "Couldn't update ticket"})

# Delete ticket
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
def delete_ticket(request : Request, ticket_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})  
    try:
        ticket = user_ticket.objects.get(id=ticket_id)
        msg = f"delete the following feedback {ticket.id}"
        ticket.delete()
    except Exception as e:
        return Response({"msg" : "The ticket is not found "})
    return Response({"msg":msg})
    

