# comments/models.py
from django.db import models

def upload_avatar_path(instance, filename):
    return f"avatars/{instance.name}_{filename}"

class Comment(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to=upload_avatar_path, blank=True, null=True)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_approved = models.BooleanField(default=False)  # для модерации
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating})"
