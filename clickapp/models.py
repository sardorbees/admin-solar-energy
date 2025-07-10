from django.db import models

class VisitorClick(models.Model):
    ip = models.GenericIPAddressField()
    user_agent = models.TextField()
    clicks = models.IntegerField(default=0)
    last_click = models.DateTimeField(auto_now=True)
    blocked = models.BooleanField(default=False)
    blocked_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('ip', 'user_agent')

    def __str__(self):
        return f"{self.ip} - {'Blocked' if self.blocked else 'Active'}"
