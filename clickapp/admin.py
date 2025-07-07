# security/admin.py
from django.contrib import admin
from .models import SuspiciousUser

@admin.register(SuspiciousUser)
class SuspiciousUserAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "click_count", "is_blocked", "last_click")
    search_fields = ("ip_address",)
    list_filter = ("is_blocked",)
