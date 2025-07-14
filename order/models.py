from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Принят'),
        ('pending', 'Ожидание'),
        ('cancelled', 'Отменён'),
    ]

    name = models.CharField(max_length=100)  # имя заказчика
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
