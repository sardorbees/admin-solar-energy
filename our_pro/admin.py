from django.contrib import admin
from .models import Work, Category

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completed_at')
    search_fields = ('title',)
    list_filter = ('category',)

admin.site.register(Category)
