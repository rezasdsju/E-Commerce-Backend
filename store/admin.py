from django.contrib import admin
# from . models import Category, Product, UserProfile, Order, OrderItem
from . models import Category, Product

# Register your models here.



admin.site.register(Category)

admin.site.register(Product)



#########++ Viewing tabulated format in DataBase
'''
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #list_display = ['id','name', 'slug']
'''
'''
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #list_display = ['id', 'category', 'name', 'description', 'price', 'image', 'created_at']
    list_display = ['category', 'name', 'description', 'price', 'image', 'created_at']
'''