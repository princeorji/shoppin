from django.shortcuts import get_object_or_404, redirect, render
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all().order_by('-date')
    return render(request, 'index.html', {'products': products})

def cart(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'cart.html', {'orders': orders})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(user=request.user, product=product)
    order.quantity += 1
    order.save()
    return redirect('cart')
   
def sub_from_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order, created = Order.objects.get_or_create(user=request.user, product=product)
    order.quantity -= 1
    order.save()
    
    if order.quantity <= 0:
        order.delete()
    return redirect('cart')