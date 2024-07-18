# import json
# from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

# def api_home(request, *args, **kwargs):

    # body = request.body 
    # # print(body) # byte string of JSON data

    # print(request.GET) # url query params
    # data = {}
    # try: # we make this try because if the body doean't have any json data don't make an server error
    #     data = json.loads(body) # string of JSON data -> pthon dictionary
    # except:
    #     pass

    # print(data) # to convert it from this string into actual python dictionary 
    # print(data.keys()) # to only print the key
    # # data['headers'] = request.headers # can't turn that headers dict back into json because is not a json serializable and can't be automatically be converted into json data
    # data['headers'] = dict(request.headers) # that will fix the error and return it to dict by making it manually
    # data['params'] = dict(request.GET)
    # data['content_type'] = request.content_type
    
    # # return JsonResponse({'message':'hello message from django api view'}) # raw data
    # return JsonResponse(data) # to return json dictionary itself
########################################################################################
# doing it with django

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data ={}
#     if model_data:
#         # we can do it manually like that 

#         # data['title'] = model_data.price
#         # data['content']= model_data.content
#         # data['price'] = model_data.price

#         # or by importing model_to_dict from django.forms.models
#         data = model_to_dict(model_data, fields = ['id', 'title']) # we can select the fields we need


#     return JsonResponse(data) # to return json dictionary itself
########################################################################################
# doing it with django restframework but without serializer

# @api_view(["GET"])   # now we can declare what method we want to allow
# def api_home(requests, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#        data = model_to_dict(model_data, fields=['id', 'price', 'sale_price']) # the sale_price will not be showen we nwwd sort of stuff to make this showen and that is the rason we make a serializer file

#     return Response(data)
########################################################################################33
# doing it with django restframework with serializer

# GET METHOD
# @api_view(["GET"])
# def api_home(request, *args, **kwargs):

#     instance = Product.objects.all().order_by("?").first()
#     data = {}

#     if instance:
#         data = ProductSerializer(instance).data


#     return Response(data)

# POST METHOD

@api_view(['POST'])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True): # rasie_exeptio to make the clien know that he is messing up


        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"data is not good"}, status=400) # if we don't watnt the client to know the error