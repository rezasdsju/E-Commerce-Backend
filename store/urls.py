from django.urls import path

from . import views
urlpatterns = [
    path('products/', views.get_products),
    path('categories/', views.get_categories),
    
    path('products/<int:pk>/', views.get_product),
    
    ####URL for Function-Based View (FBV) API that returns JSON response. 
    ####Included for Practice/Test purpose only 
    path('get_categories_json_api/', views.get_categories_json_api), 
    
    path('cart/', views.get_cart),
    path('cart/add/', views.add_to_cart),
    path('cart/remove/', views.remove_from_cart),
    path('cart/update/', views.update_cart_quantity),
]
