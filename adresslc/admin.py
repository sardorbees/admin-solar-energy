from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'country', 'region', 'city', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'city')
    list_filter = ('country', 'region')
