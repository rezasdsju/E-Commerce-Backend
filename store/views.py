from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.



def home(request):
    data = {
        'messege': 'Welcome to E-Commerce Store'
    }
    return JsonResponse(data)