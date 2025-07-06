# promotions/models.py
from django.db import models
from inventory.models import Product  # Импорт модели товара

class Promotion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='promotions')
    title = models.CharField(max_length=255)
    discount_percent = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.discount_percent}%"

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
