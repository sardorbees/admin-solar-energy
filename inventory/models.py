# inventory/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField("Имя товара", max_length=255)
    total_quantity = models.PositiveIntegerField("общее_количество", default=0)
    sold_this_week = models.PositiveIntegerField("продано_на_этой_неделе", default=0)
    is_active = models.BooleanField(default=True)

    @property
    def available_quantity(self):
        return self.total_quantity - self.sold_this_week

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар скидка'
        verbose_name_plural = 'Товар скидка'
