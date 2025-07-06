# admin.py
from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'content_object', 'added_at')
    list_filter = ('user', 'content_type')
    search_fields = ('user__username',)