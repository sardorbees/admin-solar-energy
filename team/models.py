# team/models.py
from django.db import models

class TeamMember(models.Model):
    full_name = models.CharField("Полное Имя",max_length=255)
    age = models.PositiveIntegerField("Возраст")
    profession = models.CharField("Профессия", max_length=255)
    photo = models.ImageField("Фото", upload_to='team_photos/')
    telegram_number = models.CharField("Телеграмма_Номер", max_length=20, blank=True, null=True)
    telegram_username = models.CharField("Имя_Пользователя_Телеграммы", max_length=100, blank=True, null=True)
    instagram_link = models.URLField("instagram_aккоунт", blank=True, null=True)
    facebook_link = models.URLField("facebook_aккоунт", blank=True, null=True)
    created_at = models.DateTimeField("Когда создан", auto_now_add=True)

    def __str__(self):
        return self.full_name
    

    class Meta:
        verbose_name = 'Наша команда'
        verbose_name_plural = 'Наша команда'
