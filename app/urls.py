from django.urls import path
from . import views

app_name = 'marketing'

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name="add"),
    path('sub_from_cart/<int:pk>/', views.sub_from_cart, name="subtract"),  
]