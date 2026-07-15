from rest_framework import serializers
from . models import Product, Category, CartItem, Cart






####Serializer for Function-Based View (FBV) API that returns JSON response. 
####Included for Practice/Test purpose only
class CategorySerializerApi(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    slug = serializers.SlugField()    









class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    
    class Meta:
        model = Product
        fields = '__all__'        
        
        
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only = True)
    product_image = serializers.ImageField(source='product.image', read_only=True)
    
    class Meta:
        model = CartItem
        #fields = ['id', 'product', 'product_name', 'product_price', 'product_image', 'quantity']
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only = True)
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    
    class Meta:
        model = Cart
        fields = '__all__'
        
  
  