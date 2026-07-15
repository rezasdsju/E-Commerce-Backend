from django.contrib import admin
# from . models import Category, Product, UserProfile, Order, OrderItem
from . models import Category, Product, UserProfile, Order, OrderItem, Cart, CartItem

# Register your models here.



admin.site.register(Category)

admin.site.register(Product)

admin.site.register(UserProfile)
admin.site.register(Order)

admin.site.register(OrderItem)

admin.site.register(Cart)

admin.site.register(CartItem)




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
'''
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'address']
    list_display = ['id', 'user', 'phone', 'address']'''
    
'''    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'total_amount']'''
    
'''    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    #list_display = ['id', 'order', 'product', 'quantity', 'price']
    #list_display = ['order', 'product', 'quantity', 'price']'''
    
'''    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']'''
    
    
'''@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']'''