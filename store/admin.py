from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category, ProductImage, CategoryImage

# --- INLINE ADMIN CLASSES ---

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 1


# --- MAIN ADMIN REGISTRATIONS ---

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CategoryImageInline]
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_preview', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="object-fit:cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'


@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_preview']
    prepopulated_fields = {'slug': ('name',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="object-fit:cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'
