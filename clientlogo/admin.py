from django.contrib import admin
from .models import ClientLogo

@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ['name']
