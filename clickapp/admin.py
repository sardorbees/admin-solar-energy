from django.contrib import admin
from .models import IPClick, BlockedIP

admin.site.register(IPClick)
admin.site.register(BlockedIP)
