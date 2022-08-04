from .serializers import StoreSerializer
from .models import Store
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status

# Create your views here.


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create(request: Request):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('stores.add_store'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    store_serializer = StoreSerializer(data=request.data)
    store_serializer.set_owner(request)
    if store_serializer.is_valid():
        store_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": store_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": f"Store created with id {store_serializer.data['id']}."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def read(request: Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_stores = Store.objects.filter(
            name__startswith=search_phrase)[skip:get]
    else:
        all_stores = Store.objects.all()[skip:get]

    return Response(
        {
            "msg": 'list of stores',
            "stores": StoreSerializer(instance=all_stores, many=True).data,
            "count": len(all_stores)
        },
        status=status.HTTP_200_OK
    )


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update(request: Request, store_id):
    try:
        store = Store.objects.get(id=store_id)
    except Exception as e:
        return Response(
            {
                "msg": "Store not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('stores.change_store'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.id == store.owner.id:
        return Response(
            {
                "msg": "You are not the store owner.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    store_serializer = StoreSerializer(instance=store, data=request.data)
    store_serializer.set_owner(request)
    if store_serializer.is_valid():
        store_serializer.save()
    else:
        return Response(
            {
                "msg": "Invalid.",
                "error": store_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "Store updated."
        },
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete(request: Request, store_id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {
                "msg": "please login.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    if not user.has_perm('stores.change_store'):
        return Response(
            {
                "msg": "You don't have permission.",
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        store = Store.objects.get(id=store_id)
        if not user.id == store.owner.id:
            return Response(
                {
                    "msg": "You are not the store owner.",
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        store.delete()
    except Exception as e:
        return Response(
            {
                "msg": "Store not found.",
            },
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(
        {
            "msg": "Store deleted."
        },
        status=status.HTTP_200_OK
    )
