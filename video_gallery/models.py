# video_gallery/models.py
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
