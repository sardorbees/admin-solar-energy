from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    iframe = models.TextField(help_text="Вставьте HTML iframe-код карты")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Локация-места'
        verbose_name_plural = 'Локация-места'
    