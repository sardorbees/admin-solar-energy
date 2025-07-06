from django.db import models

class YourModel(models.Model):
    name = models.CharField("Локация",max_length=255)

    class Meta:
        verbose_name = 'Локация text для сайта'
        verbose_name_plural = 'Локация text для сайта'