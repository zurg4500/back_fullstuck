from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify


class Product(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='products')
    quantity = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=False)
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
