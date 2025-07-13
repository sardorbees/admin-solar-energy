from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.cache import cache
from pytz import timezone as django_timezone

from .models import Application
from .serializers import ApplicationSerializer
import requests

TELEGRAM_TOKEN = '7614226832:AAGUGKTBy0J5HpBj9Pyuh4uUIco2GTmWADE'
TELEGRAM_CHAT_ID = '7139975148'

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def create(self, request, *args, **kwargs):
        ip = get_client_ip(request)
        phone = request.data.get('phone')
        redis_key = f'form_block_ip_{ip}'
        one_hour_ago = timezone.now() - timedelta(hours=1)

        # Redis: IP уже есть — отказ
        if cache.get(redis_key):
            return Response(
                {"detail": "Вы уже отправляли заявку. Повторите через 1 час."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # IP + номер совпадают в течение часа — отказ
        if Application.objects.filter(
            phone=phone,
            ip_address=ip,
            created_at__gte=one_hour_ago
        ).exists():
            return Response(
                {"detail": "С этого номера и IP уже отправляли заявку. Повторите через 1 час."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        # Добавим IP в сериализатор
        data = request.data.copy()
        data['ip_address'] = ip

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Заблокируем IP на 1 час в Redis
        cache.set(redis_key, '1', timeout=60 * 60)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        application = serializer.save()
        self.send_telegram_notification(application)

    def send_telegram_notification(self, application):
        # Часовой пояс Узбекистана
        uz_time = datetime.now(django_timezone('Asia/Tashkent'))
        if 9 <= uz_time.hour <= 20:  # Только с 9:00 до 20:00
            message = (
                f"📥 Новая заявка на дезинфекцию\n"
                f"👤 Имя: {application.full_name}\n"
                f"📞 Телефон: {application.phone}\n"
                f"🏠 Адрес: {application.address}\n"
                f"📝 Описание: {application.description}\n"
                f"🌐 IP: {application.ip_address}"
            )
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})

from rest_framework.views import APIView
class UnlockIPView(APIView):
    def get(self, request, *args, **kwargs):
        ip = get_client_ip(request)
        redis_key = f'form_block_ip_{ip}'
        cache.delete(redis_key)
        return Response({"detail": "IP разблокирован. Можно повторно отправить форму."}, status=200)


import requests
from django.conf import settings

def verify_recaptcha(token):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': token
    }
    resp = requests.post(url, data=data).json()
    return resp.get('success'), resp.get('score', 0.0)