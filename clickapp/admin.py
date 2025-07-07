from django.contrib import admin
from .models import ClickBlock

@admin.register(ClickBlock)
class ClickBlockAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'click_count', 'blocked', 'created_at')
    list_filter = ('blocked',)
