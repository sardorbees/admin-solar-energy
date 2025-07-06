from django.contrib import admin
from category_title.models import *
# Register your models here.

@admin.register(CategoryTitle)
class CategoryTitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')