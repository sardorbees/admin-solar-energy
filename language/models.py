from django.db import models

class Language(models.Model):
    name = models.CharField("Язык", max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'