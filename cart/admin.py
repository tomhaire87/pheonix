from django.contrib import admin

class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'quantity' 'product']
