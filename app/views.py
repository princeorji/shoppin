from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all().order_by('-date')
    return render(request, 'index.html', {'products': products})