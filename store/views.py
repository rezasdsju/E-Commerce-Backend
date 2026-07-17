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
from . models import Product, Category, Cart, CartItem
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer, CartSerializer


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


@api_view(['GET'])
def get_product(request, pk):
    try: 
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, context= {'request': request})
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error':'Product not found'}, status=404)
        
    





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




@api_view(['GET'])
def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=None)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=None)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity+=1
        item.save()
    return Response({'message':'Product Added to Cart', "cart":CartSerializer(cart).data})    
    serializer = CartSerializer(cart)
    
    
    




@api_view(['POST'])
def update_cart_quantity(request):
    item_id = request.data.get('item_id')
    quantity = request.data.get('quantity')
    
    if not item_id and quantity is None:
        return Response({'error':'Item ID and quantity are required'}, status=400)
    try:
        item = CartItem.objects.get(id=item_id)
        if int(quantity)<1:
            item.delete()
            return Response({'error':'Quantity must be at least 1'}, status=400)
        item.quantity = quantity
        item.save()
        seralizer = CartSerializer(item)
        return Response(seralizer.data)
    except CartItem.DoesNotExist:
        return Response({'error':'Cart Item not found'}, status=404)
    
    
    

@api_view(['POST'])
def remove_from_cart(request):
    item_id = request.data.get('item_id')
    CartItem.objects.filter(id=item_id).delete()
    return Response({'message':'Item removed from cart'})
