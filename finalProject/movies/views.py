from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import movie_schedule, movies_feedback, movies_info, user_ticket
from .serializers import  FeedbackSerializers, MoviesSerializers, ScheduleSerializers, TicketSerializers
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.

# Post new movie
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_movie(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.has_perm('movies.add_movie'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    movies_serializers = MoviesSerializers(data=request.data)
    if movies_serializers.is_valid():
        movies_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new movie", "errors":movies_serializers.errors}, status=status.HTTP_403_FORBIDDEN)
    return Response({"msg" : "Movie Added Successfully"}, status=status.HTTP_201_CREATED)

# List all movies
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_movie(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.list_movie'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    movie = movies_info.objects.all()
    movie_data = MoviesSerializers(instance=movie, many=True).data

    return Response({"msg" : "List of all Movies", "Movie " : movie_data})

# List all movies by genres
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_movie_bygenres(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
      return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.list_movie_bygenres'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)

    search_p = request.query_params["genres"]

    movie = movies_info.objects.all().filter(genres=search_p)
    movie_data = MoviesSerializers(instance=movie, many=True).data

    return Response({"msg" : "List of all Movies", "Movie " : movie_data})

# Update movie
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_movie(request : Request, movie_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.update_movie'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        movie = movies_info.objects.get(id=movie_id)
    except Exception as e:
        return Response({"msg" : "This movie is not found"}, status=status.HTTP_404_NOT_FOUND)

    movie_Serializer = MoviesSerializers(instance=movie, data=request.data)

    if movie_Serializer.is_valid():
        movie_Serializer.save()
        return Response({"msg" : "Movie is updated"}, status=status.HTTP_201_CREATED)
    else:
        return Response({"msg" : "Couldn't update movie"}, status=status.HTTP_403_FORBIDDEN)

# Delete Movie
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_movie(request : Request, movie_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.delete_movie'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        movie = movies_info.objects.get(id=movie_id)
        msg = f"delete the following movie {movie.name}"
        movie.delete()
    except Exception as e:
        return Response({"msg" : "The movie is not found "} ,status=status.HTTP_404_NOT_FOUND)
    return Response({"msg":msg}, status = status.HTTP_200_OK)
    
# Post new Schedule
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_schedule(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.add_schedule'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    Schedule_serializers = ScheduleSerializers(data=request.data)
    if Schedule_serializers.is_valid():
        Schedule_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new Schedule", "errors":Schedule_serializers.errors},status=status.HTTP_404_NOT_FOUND)
    return Response({"msg" : "Schedule Added Successfully"},status=status.HTTP_201_CREATED)

# List all Schedule
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_schedule(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.list_schedule'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
        

    Schedule = movie_schedule.objects.all()
    Schedule_data = ScheduleSerializers(instance=Schedule, many=True).data

    return Response({"msg" : "List of all Schedule", "Schedule " : Schedule_data})

# Update Schedule
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_schedule(request : Request, schedule_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.update_schedule'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
        
    
    try:
        schedule = movie_schedule.objects.get(id=schedule_id)
    except Exception as e:
        return Response({"msg" : "This schedule is not found"},status = status.HTTP_404_NOT_FOUND)

    schedule_Serializer = ScheduleSerializers(instance=schedule, data=request.data)

    if schedule_Serializer.is_valid():
        schedule_Serializer.save()
        return Response({"msg" : "Schedule is updated"}, status= status.HTTP_200_OK)
    else:
        return Response({"msg" : "Couldn't update schedule"}, status = status.HTTP_403_FORBIDDEN)

# Delete Schedule
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_schedule(request : Request, schedule_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.delete_schedule'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
            
    try:
        schedule = movie_schedule.objects.get(id=schedule_id)
        msg = f"delete the following director {schedule.id}"
        schedule.delete()
    except Exception as e:
        return Response({"msg" : "The schedule is not found "}, status = status.HTTP_404_NOT_FOUND)
    return Response({"msg":msg})
    
# Post new Ticket
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_ticket(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.add_ticket'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
                
    ticket_serializers = TicketSerializers(data=request.data)
    if ticket_serializers.is_valid():
        ticket_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new ticket", "errors":ticket_serializers.errors}, status = status.HTTP_403_FORBIDDEN)
    return Response({"msg" : "Your ticket Added Successfully"}, status = status.HTTP_201_CREATED)

# List all tickets
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_ticket(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"}) 

    if not user.has_perm('movies.list_ticket'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
    
    ticket = user_ticket.objects.all()
    ticket_data = TicketSerializers(instance=ticket, many=True).data

    return Response({"msg" : "List of all Users Ticket", "User Ticket " : ticket_data}) 

# Update Ticket
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_ticket(request : Request, ticket_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})  

    if not user.has_perm('movies.update_ticket'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
        
    try:
        ticket = user_ticket.objects.get(id=ticket_id)
    except Exception as e:
        return Response({"msg" : "This ticket is not found"}, status = status.HTTP_404_NOT_FOUND)

    ticket_Serializer = TicketSerializers(instance=ticket, data=request.data)

    if ticket_Serializer.is_valid():
        ticket_Serializer.save()
        return Response({"msg" : "Ticket is updated"}, status = status.HTTP_200_OK)
    else:
        return Response({"msg" : "Couldn't update ticket"}, status = status.HTTP_403_FORBIDDEN)

# Delete ticket
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_ticket(request : Request, ticket_id):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})  

    if not user.has_perm('movies.delete_ticket'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
         
    try:
        ticket = user_ticket.objects.get(id=ticket_id)
        msg = f"delete the following feedback {ticket.id}"
        ticket.delete()
    except Exception as e:
        return Response({"msg" : "The ticket is not found "}, status = status.HTTP_404_NOT_FOUND)
    return Response({"msg":msg})
    
# Post new Feedback
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_feedback(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})

    if not user.has_perm('movies.add_feedback'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
          
    feedback_serializers = FeedbackSerializers(data=request.data)
    if feedback_serializers.is_valid():
        feedback_serializers.save()
    else:
        return Response ({"msg" : "Couldn't create new feedback", "errors":feedback_serializers.errors}, status = status.HTTP_403_FORBIDDEN)
    return Response({"msg" : "Your feedback Added Successfully"}, status = status.HTTP_201_CREATED)

# List all feedbacks
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_feedback(request : Request):
    #authenticated user info is stored in request.user
    user = request.user

    if not user.is_authenticated:
        return Response({"msg" : "Please Log In"})   

    if not user.has_perm('movies.list_feedback'):
        return Response({"msg" : "You don't have movies control permission! contact your admin"}, status=status.HTTP_401_UNAUTHORIZED)
      
    search_p = request.query_params["search"]

    feedback = movies_feedback.objects.all().filter(movie=search_p)
    feedback_data = FeedbackSerializers(instance=feedback, many=True).data

    return Response({"msg" : "List of all Custmers's feedback", "Feedback :" : feedback_data})



