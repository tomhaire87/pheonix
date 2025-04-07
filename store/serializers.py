from rest_framework import serializers
from .models import Product, ProductOptionGroup, ProductOption, ProductImage, Category

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['id', 'name', 'price', 'sku']

class ProductOptionGroupSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = ProductOptionGroup
        fields = ['id', 'name', 'required', 'options']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'name', 'image', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    option_groups = ProductOptionGroupSerializer(many=True, read_only=True)
    productimage_set = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'option_groups', 'productimage_set']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']