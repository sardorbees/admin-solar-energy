from django.contrib import admin
from category_title_text.models import *
# Register your models here.

@admin.register(Category_Title_Text)
class CategoryTitleTextAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')