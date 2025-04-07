from django.db import models
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=50, unique=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    # image = models.ImageField(upload_to='static\images', default='images/default.png')
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    # REPLACE WITH REVERSE 
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, null=True, related_name='store', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, null=True)
    # image_main = models.ImageField(upload_to='static\images', default='images/default.png')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    # REPLACE WITH REVERSE 
    def get_absolute_url(self):
        return f'/shop/{self.slug}'

class ProductOptionGroup(models.Model):
    product = models.ForeignKey(Product, related_name='option_groups', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g. Wheelbase, Lights
    required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.name} ({'Required' if self.required else 'Optional'})"


class ProductOption(models.Model):
    group = models.ForeignKey(ProductOptionGroup, related_name='options', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)  # e.g. MWB, LWB, 2x Lights
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    sku = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.group.name} - {self.name} (£{self.price})"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=False, null=False)
    image = models.ImageField(upload_to='static\images', default='images/default.png')
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CategoryImage(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('', 'Unspecified'),   # <--- this adds the "not tagged" option
        ('header', 'Header'),
        ('thumbnail', 'Thumbnail'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='category_images/', default='category_images/default.png')
    slug = models.SlugField(max_length=50)
    image_type = models.CharField(
        max_length=10,
        choices=IMAGE_TYPE_CHOICES,
        blank=True,
        null=True,
        default=''
    )

    def __str__(self):
        return f"{self.name} ({self.image_type or 'Unspecified'})"