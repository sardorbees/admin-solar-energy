from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'clicks', 'is_blocked', 'created_at')
    list_filter = ('is_blocked',)
