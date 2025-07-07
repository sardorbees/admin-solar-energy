from django.db import models
from django.utils import timezone


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    clicks = models.PositiveIntegerField(default=0)
    is_blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {'Blocked' if self.is_blocked else 'Allowed'}"
