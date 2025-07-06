from django.contrib import admin
from .models import Company
from django.utils.html import format_html

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_logo', 'website', 'created_at')
    search_fields = ('name',)

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" />', obj.logo.url)
        return "No Logo"

    display_logo.short_description = 'Logo'

admin.site.register(Company, CompanyAdmin)
