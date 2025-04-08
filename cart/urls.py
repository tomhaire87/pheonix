from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart),
    path('cart/', views.get_or_create_cart),
    path('cart/add/', views.add_to_cart),
    path('cart/update/', views.update_cart_item),
    path('cart/remove/', views.remove_from_cart),
]

