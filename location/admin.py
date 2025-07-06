from django.contrib import admin
from .models import YourModel  # Replace with your actual model

@admin.register(YourModel)  # Register the model with the admin site
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.register(YourModelAdmin)