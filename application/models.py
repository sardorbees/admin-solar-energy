from django.db import models

class Application(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.phone}"
