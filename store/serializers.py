from rest_framework import serializers
from .models import Product, ProductOptionGroup, ProductOption, ProductImage, Category, CategoryImage, Review

class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['id', 'name', 'price', 'sku']

class ProductOptionGroupSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, read_only=True)

    class Meta:
        model = ProductOptionGroup
        fields = ['id', 'name', 'required', 'options','image_type']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'name', 'slug', 'image', 'image_type']


class ProductSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'thumbnail']

    def get_thumbnail(self, obj):
        thumb = obj.productimage_set.filter(image_type='thumbnail').first()
        if thumb:
            request = self.context.get('request')
            return request.build_absolute_uri(thumb.image.url) if request else thumb.image.url
        return None


class CategorySerializer(serializers.ModelSerializer):
    header_image = serializers.SerializerMethodField()
    thumbnail_image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'header_image', 'thumbnail_image']

    def get_header_image(self, obj):
        image = obj.categoryimage_set.filter(image_type='header').first()
        return image.image.url if image and image.image else None

    def get_thumbnail_image(self, obj):
        image = obj.categoryimage_set.filter(image_type='thumbnail').first()
        return image.image.url if image and image.image else None

class ProductListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'thumbnail']

    def get_thumbnail(self, obj):
        thumb = obj.productimage_set.filter(image_type='thumbnail').first()
        if thumb:
            request = self.context.get('request')
            return request.build_absolute_uri(thumb.image.url) if request else thumb.image.url
        return None

class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'products']

    def get_products(self, obj):
        request = self.context.get('request')  # <- grabs the request
        return ProductListSerializer(obj.store.all(), many=True, context={'request': request}).data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'content', 'created_at', 'stars']