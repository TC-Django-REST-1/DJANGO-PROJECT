from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# from rest_framework_simplejwt.tokens import AccessToken

from .models import Brand,BrandHistory,GeneralClasses,Categories,BrandsClasses#,Car
from .serializers import BrandSerilizer,BrandHistorySerilizer,GeneralClassesSerilizer,CategoriesSerilizer,BrandsClassesSerilizer#,CarSerilizer

def brandHistory(user,update):
    '''It's an event function that save a record for any update take place in the brand model, to reviwe later
    to see what the deffirences between before and after update, who did that update, & when that update take place'''
    
    u_brand_id = update.data["id"]
    u_brand_name = update.data["brand"]
    u_description = update.data["description"]
    u_established_in = update.data["established_in"]
    u_origin = update.data["origin"]
    u_founder = update.data["founder"]
    u_headquarters = update.data["headquarters"]
    u_last_revenue = update.data["last_revenue_billion"]
    u_year = update.data["year"]
    u_remarks = update.data["remarks"]
    
    new_brand_update = BrandHistory(brand_id= u_brand_id, brand_name= u_brand_name, description= u_description, 
                                    established_in= u_established_in, origin= u_origin, 
                                    founder= u_founder, headquarters= u_headquarters, 
                                    last_revenue_billion= u_last_revenue, year= u_year, 
                                    remarks= u_remarks, modified_by = user, 
                                    modification_date = datetime.today())
    new_brand_update.save()

    response_data = {
            "msg" : f"A new record has been added for {u_brand_name}"
        }
    return Response(response_data)

# --------------------------------------------------------------------------------------------------------
# Brand
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_brand(request: Request):
    user = request.user
    if user.is_authenticated:
        new_brand_serializer = BrandSerilizer(data=request.data)
        if new_brand_serializer.is_valid():
            new_brand_serializer.save()
            add_record = brandHistory( user, new_brand_serializer)
            # print(add_record.data)
        else:
            return Response({"msg" : "couldn't add a new brand", "errors" : new_brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
        return Response({"msg" : "A new brand added Successfully!", "msg2" : add_record.data}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def brand_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        brands = Brand.objects.filter(brand__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        brands = Brand.objects.order_by("-id").all()[skip:get]

    data = BrandSerilizer(brands, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def brand_history_record(request: Request):
        if "search" in request.query_params:
            search_phrase = request.query_params["search"]
            skip = int(request.query_params.get("skip", 0))
            get = int(request.query_params.get("get", 10))
            brands = BrandHistory.objects.filter(brand_name__startswith=search_phrase)[skip:get]
        else:
            skip = int(request.query_params.get("skip", 0))
            get = int(request.query_params.get("get", 10))
            brands = BrandHistory.objects.order_by("-id").all()[skip:get]

        data = BrandHistorySerilizer(brands, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    


@api_view(['PUT'])
def update_brand(request: Request, brand_id):
    user = request.user
    try:
        brand = Brand.objects.get(id = brand_id)
        data = BrandSerilizer(instance=brand, data=request.data)
        if data.is_valid():
            data.save()
            add_record = brandHistory( user, data)
            return Response({"msg" : "Brand updated successfully", "msg2" : add_record.data}, status=status.HTTP_200_OK)
        else:
            return Response({"msg" : "couldn't update the brand", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"msg" : f"The brand with ID No:{brand_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id = brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : f"The brand with ID No:{brand_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"A brand with ID No:{brand_id} has been deleted successfully"}, status=status.HTTP_200_OK)


# --------------------------------------------------------------------------------------------------------
# General Classes
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_general_class(request: Request):
    new_class_serilizer = GeneralClassesSerilizer(data=request.data)
    if new_class_serilizer.is_valid():
        new_class_serilizer.save()
    else:
        return Response({"msg" : "couldn't add a new general class", "errors" : new_class_serilizer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "A new general class created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAdminUser])
def general_class_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        g_class = GeneralClasses.objects.filter(general_class__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        g_class = GeneralClasses.objects.order_by("-id").all()[skip:get]

    data = GeneralClassesSerilizer(g_class, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def update_general_class(request: Request, general_class_id):
    # user = request.user
    try:
        g_class = GeneralClasses.objects.get(id = general_class_id)
        data = GeneralClassesSerilizer(instance=g_class, data=request.data)
        if data.is_valid():
            data.save()
            return Response({"msg" : "General class updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg" : "couldn't update the class", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"msg" : f"The class with ID No:{general_class_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def remove_general_class(request: Request, general_class_id):
    try:
        g_class = GeneralClasses.objects.get(id = general_class_id)
        g_class.delete()
    except Exception as e:
        return Response({"msg" : f"The brand with ID No:{general_class_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"A brand with ID No:{general_class_id} has been deleted successfully"}, status=status.HTTP_200_OK)




# --------------------------------------------------------------------------------------------------------
# Brands Classes
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_brands_class(request: Request):
    new_brand_class_serilizer = BrandsClassesSerilizer(data=request.data)
    if new_brand_class_serilizer.is_valid():
        new_brand_class_serilizer.save()
    else:
        return Response({"msg" : "couldn't add a new brand class", "errors" : new_brand_class_serilizer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "A new brand class created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAdminUser])
def brands_class_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        b_class = BrandsClasses.objects.filter(class_name__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        b_class = BrandsClasses.objects.order_by("-id").all()[skip:get]

    data = BrandsClassesSerilizer(b_class, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAdminUser])
def update_brands_class(request: Request, brand_class_id):
    # user = request.user
    try:
        b_class = BrandsClasses.objects.get(id = brand_class_id)
        data = BrandsClassesSerilizer(instance=b_class, data=request.data)
        if data.is_valid():
            data.save()
            return Response({"msg" : "Brand class updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg" : "couldn't update this brand class", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"msg" : f"The class with ID No:{brand_class_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAdminUser])
def remove_brands_class(request: Request, brand_class_id):
    try:
        b_class = BrandsClasses.objects.get(id = brand_class_id)
        b_class.delete()
    except Exception as e:
        return Response({"msg" : f"The brand class with ID No:{brand_class_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"The brand class with ID No:{brand_class_id} has been deleted successfully"}, status=status.HTTP_200_OK)


# --------------------------------------------------------------------------------------------------------
# Categories
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def add_new_Category(request: Request):
    new_category_serilizer = CategoriesSerilizer(data=request.data)
    if new_category_serilizer.is_valid():
        new_category_serilizer.save()
    else:
        return Response({"msg" : "couldn't add a new category", "errors" : new_category_serilizer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "A new category created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAdminUser])
def Categories_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        categories = Categories.objects.filter(category_name__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))
        categories = Categories.objects.order_by("-id").all()[skip:get]

    data = CategoriesSerilizer(categories, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def update_category(request: Request, category_id):
    # user = request.user
    try:
        category = Categories.objects.get(id = category_id)
        data = CategoriesSerilizer(instance=category, data=request.data)
        if data.is_valid():
            data.save()
            return Response({"msg" : "Category updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg" : "couldn't update the category", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        return Response({"msg" : f"Category with ID No:{category_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def remove_category(request: Request, category_id):
    try:
        category = Categories.objects.get(id = category_id)
        category.delete()
    except Exception as e:
        return Response({"msg" : f"The category with ID No:{category_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"The category with ID No:{category_id} has been deleted successfully"}, status=status.HTTP_200_OK)



# # --------------------------------------------------------------------------------------------------------
# # Cars
# @api_view(['POST'])
# def add_car(request: Request):
#     new_car_serilizer = CarSerilizer(data=request.data)
#     if new_car_serilizer.is_valid():
#         new_car_serilizer.save()
#     else:
#         return Response({"msg" : "couldn't add a new car", "errors" : new_car_serilizer.errors}, status=status.HTTP_403_FORBIDDEN)

#     return Response({"msg" : "A new car created successfully"}, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def cars_list(request: Request):

#     skip = int(request.query_params.get("skip", 1))
#     get = int(request.query_params.get("get", 4))


#     cars = Car.objects.order_by("-id").all()[skip:get]
#     data = CarSerilizer(cars, many=True).data
#     return Response(data, status=status.HTTP_200_OK)

# @api_view(['PUT'])
# def update_car(request: Request, car_id):
#     car = Car.objects.get(id = car_id)
#     data = CarSerilizer(instance=car, data=request.data)
#     if data.is_valid():
#         data.save()
#         return Response({"msg" : "Car updated successfully "}, status=status.HTTP_200_OK)
#     else:
#         return Response({"msg" : "couldn't update the car", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def remove_car(request: Request, car_id):
#     try:
#         car = Car.objects.get(id = car_id)
#         car.delete()
#     except Exception as e:
#         return Response({"msg" : f"The car with ID No:{car_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

#     return Response({"msg" : f"A car with ID No:{car_id} has been deleted successfully"}, status=status.HTTP_200_OK)




# @api_view(['GET'])
# def brand_cars_list(request: Request, brand_name):
#     try:
#         brand = Brand.objects.get(name = brand_name) # get the whole info of brand by its brand_name so we can extract the id of that brand
#         cars = Car.objects.filter(brand__exact=brand.id) # filter all products by the brand.id because the Product model has only the id of the brand not the name
#         data = CarSerilizer(cars, many=True).data
#         return Response(data, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"msg" : f"The brand with ID No:{brand_name} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)