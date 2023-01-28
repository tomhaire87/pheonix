from django.shortcuts import render
from .models import Product, Category

def get_products(request):
    products = Product.objects.all()
    return render(request, products/index.html, {'products':products})