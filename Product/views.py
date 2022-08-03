from wsgiref import validate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models.functions import Lower
from rest_framework import status

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Brand, Product
from .serializers import ProductSerializer, BrandSerializer


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_brand(request: Request):

    new_brand = BrandSerializer(data=request.data)
    if new_brand.is_valid():
        new_brand.save()
    else:
        print(request.data["brand_name"])
        return Response({
            "msg": new_brand.errors, "details": (new_brand.data.values())
        }, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({
        "msg": f"create a new brand with brand_name {{ {new_brand.data.get('brand_name')} }} Successfully"
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_brand(request: Request):

    # returns the total count of Brand in the database, for testing only
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_brands = Brand.objects.filter(
            brand_name=search_phrase).values()
    else:
        all_brands = Brand.objects.order_by(Lower("brand_name"))
    brand = BrandSerializer(instance=all_brands,
                            data=all_brands.values(), many=True)
    brand.is_valid()
    res_data = {
        "msg": "A list of All brands",
        "brands": list(brand.data)[skip:get]
    }
    return Response(res_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_brand(request: Request, brand_name: str):
    try:
        data_obj = Brand.objects.get(brand_name=brand_name)
        print(type(data_obj))
    except Brand.DoesNotExist:
        return Response({"msg": f"The brand {brand_name} does not exist"},
                        status=status.HTTP_404_NOT_FOUND)

    data = BrandSerializer(instance=data_obj, data=request.data)
    if data.is_valid():
        data.save()
        return Response({"msg": {"Your brand": data_obj.to_dict(), "is updated to": data.data}}, status=status.HTTP_202_ACCEPTED)
    else:
        print(data.errors)
        return Response({"msg": data.errors}, status=status.HTTP_304_NOT_MODIFIED)


@api_view(["DELETE"])
def delete_brand(request: Request, brand_name):

    try:
        brand = Brand.objects.get(brand_name=brand_name)
        brand.delete()
    except Brand.DoesNotExist:
        return Response({"msg": f"The brand {brand_name} is not Found!"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg": f"delete the following brand {brand_name}"}, status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def add_Product(request: Request):

    brand = request.data.get('brand_name')
    product_name = request.data.get('product_name')
    type = request.data.get('type')
    price = request.data.get('price')
    quantity = request.data.get('quantity')
    is_active = request.data.get('is_active')
    try:
        Prod = Product()
        Prod.brand = Brand.objects.get(brand_name=brand)
        Prod.product_name = product_name
        Prod.price = price
        Prod.type = type
        Prod.quantity = quantity
        Prod.is_active = is_active
        Prod.save()
    except Exception as e:
        return Response({"msg": e}, status=status.HTTP_406_NOT_ACCEPTABLE)
    # new_Product = ProductSerializer(
    #     instance=Product, data=request.data, many=True,)
    # if new_Product.is_valid():
    #     new_Product.save()
    # else:
    #     print(new_Product.data)
    #
    # print(new_Product.data.get('name'))
    # # {{ {new_Product.data.get('name')} }} {request.data.get['brand']}
    return Response({
        "msg": f"create a new product in brand {{{brand }}} with name {{{product_name}}}  Successfully"
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_Products(request: Request):

    # returns the total count of Products in the database, for testing only
    print(Product.objects.count())

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))
    all_Product = Product.objects.order_by(Lower("product_name"))
    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_Product = Product.objects.all().filter(brand_name=search_phrase)
        product = ProductSerializer(data=all_Product, many=True)
        product.is_valid()
        res_data = {
            "msg": f"A list of All Products of the brand {search_phrase} ",
            "product": product.data[skip:get]
        }
    else:
        product = ProductSerializer(data=all_Product, many=True)
        product.is_valid()
        res_data = {
            "msg": "A list of All Product",
            "Product": product.data[skip:get]
        }

    return Response(res_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request: Request, product_id: str):

    data_obj = Product.objects.get(id=product_id)
    data = ProductSerializer(data_obj, request.data)
    if data.is_valid():
        print(data)
        data.save()
        return Response({"msg": "Your prodect is updated!", "Details": data.data})
    else:
        print(data.errors)
        return Response({"msg": data.errors})


@api_view(["DELETE"])
def delete_product(request: Request, product_id):

    try:
        product: Product = Product.objects.get(id=product_id)
        print(product.product_name+"  "+product.brand)
        product.delete()
    except Exception as e:
        print(e)
        return Response({"msg": f"The product is not Found!"})

    return Response({"msg": f"delete the following product {product}"})
