# products/admin.py
from django.contrib import admin
from .models import Category, Product, Power, ProductType, Brand, SolarPanel


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Power)
class PowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'price', 'old_price', 'installment_price',
        'color', 'tag', 'rating', 'reviews', 'in_stock', 'is_available', 'views', 'power'
    )
    list_filter = ('category', 'color', 'tag', 'in_stock', 'is_available', 'power')
    search_fields = ('name', 'description', 'color', 'tag')
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('views',)
    ordering = ('-id',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'rating', 'price']
    prepopulated_fields = {'slug': ('name', 'rating', 'price')}
    search_fields = ['name', 'rating', 'price']


@admin.register(SolarPanel)
class SolarPanelAdmin(admin.ModelAdmin):
    list_display = ('name', 'power', 'price')
    list_filter = ('power',)
    search_fields = ('name',)
