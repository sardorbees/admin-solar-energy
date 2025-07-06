from django.core.management.base import BaseCommand
from promotions.models import Promo
from django.utils import timezone
from django.db.models import F
from datetime import timedelta

class Command(BaseCommand):
    help = "Удаляет просроченные акции (старше 24ч)"

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_promos = Promo.objects.filter(created_at__lt=now - F('duration'))
        count = expired_promos.count()
        expired_promos.delete()
        self.stdout.write(self.style.SUCCESS(f"Удалено {count} просроченных акций"))
