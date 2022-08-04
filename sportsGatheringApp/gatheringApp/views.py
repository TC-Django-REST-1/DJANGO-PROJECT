from datetime import datetime
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from .models import gather, GatherPlayers
from .serializers import gatherSerializer
from users.models import userInfo

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

@api_view(['GET'])
def get_all_gathers(request : Request):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))
    gathers = gather.objects.all()

    gathers_data = gatherSerializer(instance=gathers, many=True).data[skip:get]

    res = {
        'msg': 'all the gathers',
        'page': skip,
        'gathers':gathers_data,
    }
    return Response(data=res, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_gather(request : Request):
    
    user = request.user
    if not user.is_authenticated:
        return Response({"msg": "Please log in"},status=status.HTTP_403_FORBIDDEN)
    
    data = request.data
    data["leader"] = user.id
    data["leaderPhoneNumber"] = userInfo.objects.filter(user=user)[0].phoneNumber

    gather_serializer = gatherSerializer(data=data)

    if gather_serializer.is_valid():
        gather_serializer.save()
    else:
        return Response({
            'msg': "sorry couldn't create a gather",
            "errors": gather_serializer.errors,
        },status=status.HTTP_403_FORBIDDEN)

    return Response({"msg": "The Gather created Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_gather(request : Request, gather_id):

    user =request.user
    data =request.data

    if not user.is_authenticated:
        return Response({"msg": "Please login"},status=status.HTTP_403_FORBIDDEN)

    try:
        updated_gather = gather.objects.get(id=gather_id)
    except Exception as e:
        return Response({"msg" : "This gather is not found"}, status=status.HTTP_404_NOT_FOUND)


    if updated_gather.leader.id != user.id:
        return Response({"msg": "sorry you are not authorized to accuses the gather! just the creator can accuses"}, status=status.HTTP_403_FORBIDDEN)

    data["leader"] = user.id

    gather_serializer = gatherSerializer(instance=updated_gather,data=data)

    if gather_serializer.is_valid():
        gather_serializer.save()
    else:
        return Response(
            {
            "msg":"sorry couldn't update gather", "errors": gather_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN)

    return Response({"msg":"Gather updated successfully!"},status=status.HTTP_200_OK)



@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
def delete_gather(request : Request, gather_id):
    
    user = request.user
    
    if not user.is_authenticated:
        return Response({"msg": "Please login"},status=status.HTTP_403_FORBIDDEN)

    try:
        deleted_gather = gather.objects.get(id=gather_id)
    except Exception as e:
        return Response({"msg" : "This gather is not found"}, status=status.HTTP_404_NOT_FOUND)

    if deleted_gather.leader.id != user.id:
        return Response({"msg": "sorry you are not authorized to accuses the gather! just the creator can accuses"}, status=status.HTTP_403_FORBIDDEN)
    
    deleted_gather.delete()

    return Response({"msg": "The Gather Deleted Successfully!"},status=status.HTTP_200_OK)
    
    
@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def join_gather(request : Request, gather_id):

    user = request.user
    
    if not user.is_authenticated:
        return Response({"msg": "Please login"},status=status.HTTP_403_FORBIDDEN)
    try:
        gather_to_join = gather.objects.get(id= gather_id)
    except Exception as e:
        return Response({"msg": "Sorry the Gather Not Found!"},status=status.HTTP_404_NOT_FOUND)

    user = userInfo.objects.get(user_id=user.id)

    if gather_to_join.maxLimit == gather_to_join.currentPlayers:
        return Response({"msg": "Sorry the Gather is full!"},status=status.HTTP_403_FORBIDDEN)

    if gather_to_join.justFemales and user.isMale:
        return Response({"msg": "Sorry this Gather only for Females!"},status=status.HTTP_403_FORBIDDEN)
    

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gather_date = gather_to_join.matchDateTime.strftime("%Y-%m-%d %H:%M:%S")
    
    if datetime.strptime(now, "%Y-%m-%d %H:%M:%S") > datetime.strptime(gather_date, "%Y-%m-%d %H:%M:%S"):
        return Response({"msg": "Sorry the Gather Expired!"},status=status.HTTP_403_FORBIDDEN)
    
    new_player = GatherPlayers(user.user_id, gather_to_join.id)
    new_player.save()

    gather_to_join.currentPlayers +=  1
    gather_to_join.save()

    return Response({"msg": "you joined the Gather Successfully!"},status=status.HTTP_200_OK)


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def sort_by(request : Request):

    gathers = gather.objects.all()

    if "sport" in request.query_params:
        gathers = gathers.filter(sport=request.query_params["sport"])

    if "just_females" in request.query_params:
        gathers = gathers.filter(justFemales=request.query_params["just_females"])
    
    if "city" in request.query_params:
        gathers = gathers.filter(city=request.query_params["city"])


    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    gathers_data = gatherSerializer(instance=gathers, many=True).data[skip:get]

    res = {
        'msg': 'all the gathers',
        'page': skip,
        'gathers':gathers_data,
    }

    return Response(data=res, status=status.HTTP_200_OK)



