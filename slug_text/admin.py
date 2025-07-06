from django.contrib import admin
from .models import SlugCategory

@admin.register(SlugCategory)  # Register the model with the admin site
class SlugCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category_name')  # Adjust to your model's fields
    search_fields = ('name', 'slug', 'category_name')

admin.register(SlugCategory)