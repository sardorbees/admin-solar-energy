# team/admin.py
from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'age', 'profession', 'telegram_username', 'created_at')
    search_fields = ('full_name', 'profession', 'telegram_username')
    list_filter = ('profession', 'created_at')
