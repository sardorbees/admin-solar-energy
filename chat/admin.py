from django.contrib import admin
from .models import ChatMessage

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_bot', 'timestamp')
    list_filter = ('is_bot', 'timestamp')
    search_fields = ('message', 'user__username')
    ordering = ('-timestamp',)
