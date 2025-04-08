from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem
from store.models import Product
from .serializers import CartSerializer

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if cart_item.cart.user == request.user:
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
            cart_item.save()
    return redirect('cart:cart')

@api_view(['GET'])
def get_or_create_cart(request):
    # Ensure session is initialized
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    user = request.user if request.user.is_authenticated else None

    # Try to find existing cart
    cart = Cart.objects.filter(
        user=user if user else None,
        session_key=None if user else session_key
    ).first()

    if not cart:
        cart = Cart.objects.create(
            user=user if user else None,
            session_key=None if user else session_key
        )

    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    if not request.session.session_key:
        request.session.create()

    session_key = request.session.session_key
    user = request.user if request.user.is_authenticated else None

    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    # Get or create cart for user or guest session
    cart, _ = Cart.objects.get_or_create(
        user=user if user else None,
        session_key=None if user else session_key
    )

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += quantity
    else:
        item.quantity = quantity
    item.save()

    return Response({'success': True})

@api_view(['POST'])
def update_cart_item(request):
    item_id = request.data.get('item_id')
    quantity = int(request.data.get('quantity'))

    try:
        item = CartItem.objects.get(id=item_id, cart__user=request.user)
        item.quantity = quantity
        item.save()
        return Response({'success': True})
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)

@api_view(['POST'])
def remove_from_cart(request):
    item_id = request.data.get('item_id')
    try:
        item = CartItem.objects.get(id=item_id, cart__user=request.user)
        item.delete()
        return Response({'success': True})
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)


