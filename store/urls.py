from django.urls import path

from . import views
from .views import ProductDetailAPI ,CategoryListAPI

app_name = 'store'

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('about', views.about, name='about'),
    path('shop/<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('api/products/<slug:slug>/', ProductDetailAPI.as_view(), name='product-detail-api'),
    path('api/categories/', CategoryListAPI.as_view(), name='category-list-api'),
]