from django.db import models
from django.utils import timezone
from decimal import Decimal

class TariffPlan(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tariffs/images/')
    icon = models.ImageField(upload_to='tariffs/icons/', blank=True, null=True)
    discount_percent = models.PositiveIntegerField(default=0)
    holiday = models.CharField(max_length=255, blank=True, null=True)
    weekday = models.CharField(
        max_length=9,
        choices=[(str(i), day) for i, day in enumerate(
            ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        )],
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    def discounted_price(self):
        return self.price * (Decimal('1') - Decimal(self.discount_percent) / Decimal('100'))

    def is_today_applicable(self):
        today = timezone.localdate()
        is_weekday_match = self.weekday == str(today.weekday())
        is_holiday_match = self.holiday == "Ramadan" and today.month == 3  # Например, март — Рамадан
        return self.is_active and (is_weekday_match or is_holiday_match)

    def __str__(self):
        return self.title
