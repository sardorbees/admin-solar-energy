# admin.py
from django.contrib import admin
from .models import ClickPayment

@admin.register(ClickPayment)
class ClickPaymentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'amount', 'is_paid', 'created_at')
    list_filter = ('is_paid', 'created_at')
    search_fields = ('full_name', 'phone_number')
    readonly_fields = ('click_trans_id', 'is_paid', 'created_at')
