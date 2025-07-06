from django.contrib import admin
from .models import TariffPlan

@admin.register(TariffPlan)
class TariffPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_percent', 'holiday', 'weekday', 'is_active')
    list_filter = ('is_active', 'holiday', 'weekday')
    search_fields = ('title',)
