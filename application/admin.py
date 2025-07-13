# admin.py
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'address', 'ip_address', 'created_at')
    search_fields = ('full_name', 'phone', 'ip_address')
    list_filter = ('created_at',)
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Контактная информация", {
            "fields": ("full_name", "phone", "address")
        }),
        ("Описание заявки", {
            "fields": ("description",)
        }),
        ("Дополнительно", {
            "fields": ("created_at",)
        }),
    )
