from django.contrib import admin
from .models import VisitorClick
from django.utils.timezone import now

@admin.register(VisitorClick)
class VisitorClickAdmin(admin.ModelAdmin):
    list_display = ('ip', 'clicks', 'blocked', 'blocked_at', 'last_click')
    list_filter = ('blocked',)
    search_fields = ('ip', 'user_agent')
    actions = ['block_selected', 'unblock_selected']

    @admin.action(description="🔒 Заблокировать навсегда")
    def block_selected(self, request, queryset):
        queryset.update(blocked=True, blocked_at=now())

    @admin.action(description="✅ Разблокировать")
    def unblock_selected(self, request, queryset):
        queryset.update(blocked=False, blocked_at=None)
