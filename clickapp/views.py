# security/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import SuspiciousUser
import requests

TELEGRAM_BOT_TOKEN = '7307767852:AAG7yPzsRWCmZHkq5phcE-x8yySkW99ecxo'
TELEGRAM_CHAT_ID = '7139975148'
CLICK_THRESHOLD = 20
TIME_WINDOW_SECONDS = 10  # промежуток времени, в который считаются клики

def get_client_ip(request):
    return request.META.get("REMOTE_ADDR")

@api_view(['POST'])
def register_click(request):
    ip = get_client_ip(request)
    user, _ = SuspiciousUser.objects.get_or_create(ip_address=ip)

    now = timezone.now()
    time_diff = (now - user.last_click).total_seconds()

    if user.is_blocked:
        return Response({"blocked": True})  # уже заблокирован — не пускать

    # Считаем клики в пределах окна
    if time_diff < TIME_WINDOW_SECONDS:
        user.click_count += 1
    else:
        user.click_count = 1

    user.last_click = now

    # Блокируем навсегда при превышении порога
    if user.click_count >= CLICK_THRESHOLD:
        user.is_blocked = True
        send_telegram_alert(ip)

    user.save()
    return Response({"blocked": user.is_blocked})

def send_telegram_alert(ip):
    msg = f"🚨 Подозрение на автоклик\nIP: {ip} заблокирован навсегда."
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})