from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    '''Display these fields in the admin panel. Sort by sku.'''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'sale_price',
        'stock_quantity',
        'rating',
        'image',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    '''Display these fields in the admin panel.'''
    list_display = (
        'name',
        'friendly_name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
