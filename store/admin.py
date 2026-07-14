from django.contrib import admin
# from . models import Category, Product, UserProfile, Order, OrderItem
from . models import Category

# Register your models here.



admin.site.register(Category)

# admin.site.register(Product)
# admin.site.register(UserProfile)
# admin.site.register(Order)
# admin.site.register(OrderItem)



'''
#Viewing tabulated format in DataBase
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #list_display = ['id','name', 'slug']
'''