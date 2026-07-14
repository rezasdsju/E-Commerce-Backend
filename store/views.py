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