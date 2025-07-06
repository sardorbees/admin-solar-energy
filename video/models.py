# videos/models.py

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='video')
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Добавить_Видео'
        verbose_name_plural = 'Добавить_Видео'
