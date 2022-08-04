
import json
from django.db import IntegrityError
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
        return Response({
            "msg": f"create a new brand with brand_name {{ {new_brand.data.get('brand_name')} }} Successfully"
        }, status=status.HTTP_200_OK)
    else:
        print(request.data["brand_name"])
        return Response({
            "msg": new_brand.errors, "details": (new_brand.data.values())
        }, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(["GET"])
def list_brand(request: Request):

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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_brand(request: Request, brandy: str):
    import json
    try:
        brand_name = request.data.get('brand_name')
        established_at_Year = request.data.get('established_at_Year')
        data_obj = Brand.objects.filter(
            brand_name=brandy)
        temp = list(data_obj.all().values())[0]
        data_obj.update(brand_name=brand_name,
                        established_at_Year=established_at_Year)

        return Response({"msg": {"Your brand": temp, "is updated to": request.data}},
                        status=status.HTTP_202_ACCEPTED)

    except IntegrityError as e:
        s = str(e).split(": ")[1].split(".")[1]
        s = json.dumps(s)[1:-1]
        return Response({"msg": f"You need to put {s}"},
                        status=status.HTTP_400_BAD_REQUEST)
    except IndexError as e:
        return Response({"msg": f"the brand '{brandy}' not Found"},
                        status=status.HTTP_404_NOT_FOUND)


@ api_view(["DELETE"])
@ authentication_classes([JWTAuthentication])
@ permission_classes([IsAuthenticated])
def delete_brand(request: Request, brandy):

    try:
        brand = Brand.objects.get(brand_name=brandy)
        brand.delete()
    except Brand.DoesNotExist:
        return Response({"msg": f"The brand {brandy} is not Found!"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg": f"delete the following brand {brandy}"}, status=status.HTTP_202_ACCEPTED)


@ api_view(['POST'])
@ authentication_classes([JWTAuthentication])
@ permission_classes([IsAuthenticated])
def add_Product(request: Request):

    try:
        brand_name = request.data.get('brand_name')
        product_name = request.data.get('product_name')
        type = request.data.get('type')
        price = request.data.get('price')
        quantity = request.data.get('quantity')
        is_active = request.data.get('is_active')

    # use this mothed of creating the prodect to make sure the brand store correctly in the databse

        brand = Brand.objects.filter(brand_name=brand_name)
        if not list(brand.values_list()) == []:

            Prod = Product()
            Prod.brand: Brand = brand.get()
            Prod.product_name = product_name
            Prod.price = price
            Prod.type = type
            Prod.quantity = quantity
            Prod.is_active = is_active
            Prod.save()
            return Response({
                "msg": f"create a new product in brand {{{brand.values_list()[0][0]}}} with name {{{product_name}}}  Successfully"
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                "msg": f"the brand {{{brand_name}}} is not exists in the database"
            }, status=status.HTTP_200_OK)

    except Exception as e:
        # the error return as nested list
        error = list(e)[0][1][0]
        return Response({"msg": error}, status=status.HTTP_406_NOT_ACCEPTABLE)


@ api_view(['GET'])
def list_Products(request: Request):

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


@ api_view(['PUT'])
def update_product(request: Request, product_id: str):

    try:
        brand = Brand.objects.get(brand_name=request.data.get('brand_name'))
        product_name = request.data.get('product_name')
        type = request.data.get('type') or "Food"
        description = request.data.get('description') or ""
        image_url = request.data.get('image_url') or ""
        price = request.data.get('price') or 0.0
        quantity = request.data.get('quantity') or 1
        is_active = request.data.get('is_active') or True

        data_obj = Product.objects.filter(id=product_id)
        if not list(data_obj.values_list()) == []:
            data_obj.update(brand=brand, product_name=product_name,
                            type=type, description=description, image_url=image_url, price=price,
                            quantity=quantity, is_active=is_active)
            data = Product.objects.filter(id=product_id).values()

            return Response({"msg": "Your prodect is updated!", "Details":
                                 data.values()},status=status.HTTP_202_ACCEPTED)

        else:
            return Response({"msg": f" The ID [ {product_id} ] for the product is not Found "})
    except Exception as e:

        return Response({"msg": json.dumps(str(e))})


@ api_view(["DELETE"])
def delete_product(request: Request, product_id):

    try:
        product = Product.objects.filter(id=product_id)
        temp = list(product.values_list())
        if not temp == []:
            print(temp)
            product.delete()
            return Response({"msg": f"delete the following product {temp} Sucssesfuly"})
        else:
            return Response({"msg": f"The product is not Found!"})
    except Exception as e:
        print(e)
