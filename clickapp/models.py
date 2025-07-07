# security/models.py
from django.db import models
from django.utils import timezone

class SuspiciousUser(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    click_count = models.IntegerField(default=0)
    last_click = models.DateTimeField(default=timezone.now)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ip_address} - {'Blocked' if self.is_blocked else 'Active'}"
