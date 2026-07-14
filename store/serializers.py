from rest_framework import serializers
from . models import Product, Category






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
        
        



  
  