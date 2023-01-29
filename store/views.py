from django.shortcuts import render
from .models import Product, Category


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def get_products(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products':products})