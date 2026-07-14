'''from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    data = {
        'messege': 'Welcome to E-Commerce Store'
    }
    return JsonResponse(data)'''
    
    
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Product, Category
from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    
    
    
    
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data)



####Function-Based View (FBV) API that returns JSON response.  
####Included for Practice/Test purpose only
from django.http import HttpResponse
from .serializers import CategorySerializerApi
from rest_framework.renderers import JSONRenderer
def get_categories_json_api(request):
    #Complex data
    category = Category.objects.all()
    #Python Dictionary
    serializer = CategorySerializerApi(category, many=True)
    #Render to Json
    json_data = JSONRenderer().render(serializer.data)
    #Sent Json data to user
    return HttpResponse(json_data, content_type='application/json')