# core/admin.py
from django.contrib import admin
from .models import UserTheme

@admin.register(UserTheme)
class UserThemeAdmin(admin.ModelAdmin):
    list_display = ['user', 'theme']
    list_filter = ['theme']
    search_fields = ['user__username']
