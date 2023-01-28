from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.get_products, name='get_products')

]