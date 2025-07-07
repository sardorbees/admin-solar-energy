from django.db import models
from django.utils import timezone

class IPClick(models.Model):
    ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip

class BlockedIP(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    blocked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip
