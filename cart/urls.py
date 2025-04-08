# cart/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_or_create_cart),         # GET /api/cart/
    path('add/', views.add_to_cart),            # POST /api/cart/add/
    path('update/', views.update_cart_item),    # POST /api/cart/update/
    path('remove/', views.remove_from_cart),    # POST /api/cart/remove/
]