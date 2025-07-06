# inventory/admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_quantity', 'sold_this_week', 'available_quantity', 'is_active')
    search_fields = ('is_active', 'name',)
    list_editable = ('total_quantity', 'sold_this_week')
