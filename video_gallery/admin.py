# video_gallery/admin.py
from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video', 'created_at')
    search_fields = ('title',)
