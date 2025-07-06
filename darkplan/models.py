# core/models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class UserTheme(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(
        max_length=10,
        choices=[('light', 'Light'), ('dark', 'Dark')],
        default='light'
    )

    def __str__(self):
        return f"{self.user.username} - {self.theme}"
