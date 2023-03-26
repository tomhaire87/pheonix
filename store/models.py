from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    # REPLACE WITH REVERSE 
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='store', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True, null=True)
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
        return f'/{self.category.slug}/{self.slug}'
