from django.db import models

class ClickBlock(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    click_count = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {'Blocked' if self.blocked else 'Active'}"
