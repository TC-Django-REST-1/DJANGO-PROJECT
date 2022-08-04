from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from localmarket.models import LocalMarket
from .serializers import LocalMarketSerilizer

# Create your views here.
@api_view(['POST'])
def add_market(request: Request) -> Response:

    localmarket = LocalMarketSerilizer(data=request.data)
    
    if localmarket.is_valid():
        localmarket.save()
        return Response({"msg" : "added succefully!"})
    return Response({"msg": localmarket.errors})

@api_view(['GET'])
def get_markets(request: Request) -> Response:
    
    if "max" and "min" in request.query_params:

        maximumm = int(request.query_params.get("max"))
        minmumm = int(request.query_params.get("min"))

        markets = LocalMarket.objects.all()[minmumm:maximumm]

    elif "search" in request.query_params:
        print("went")
        market_title = request.query_params.get("search")
        localmarkets = LocalMarket.objects.filter(title=market_title)

    else:

        localmarkets = LocalMarket.objects.order_by('-id').all()

    data = LocalMarketSerilizer(markets, many=True).data

    return Response(data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_market(request: Request, market_id) -> Response:

    localmarket = LocalMarket.objects.get(id=market_id)

    data = LocalMarketSerilizer(instance= localmarket, data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response({"msg": "updated succefully"}, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def delete_market(request: Request, market_id) -> Response:

    localmarket = LocalMarket.objects.get(id=market_id)

    localmarket.delete()

    return Response({"msg":"market deleted succefully"})