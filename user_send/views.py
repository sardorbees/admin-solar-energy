from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import Visitor
from .serializers import VisitorSerializer
import requests

TELEGRAM_BOT_TOKEN = '7307767852:AAG7yPzsRWCmZHkq5phcE-x8yySkW99ecxo'
TELEGRAM_CHAT_ID = '7139975148'
CLICK_THRESHOLD = 5  # Количество кликов до блокировки

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')

class ClickTrackView(APIView):
    def post(self, request):
        ip = get_client_ip(request)
        ua = request.META.get('HTTP_USER_AGENT', '')
        visitor, _ = Visitor.objects.get_or_create(ip_address=ip, user_agent=ua)

        if visitor.is_blocked:
            return Response({'detail': 'Вы заблокированы'}, status=status.HTTP_403_FORBIDDEN)

        visitor.clicks += 1
        if visitor.clicks > CLICK_THRESHOLD:
            visitor.is_blocked = True
            visitor.save()
            self.send_alert(ip, ua)
            return Response({'detail': 'Вы были заблокированы'}, status=status.HTTP_403_FORBIDDEN)

        visitor.save()
        return Response({'detail': 'Клик зарегистрирован'}, status=status.HTTP_200_OK)

    def send_alert(self, ip, ua):
        message = f"🚨 Атака на сайт!\nIP: {ip}\nUA: {ua}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': TELEGRAM_CHAT_ID,
            'text': message
        }
        requests.post(url, data=payload)