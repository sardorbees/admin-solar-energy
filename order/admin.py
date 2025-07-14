from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'phone', 'address')
